"""
Created on Sun Jul 19 10:29:44 2026
this program is under the PolyForm Noncommercial License 10.0
@author: gemzoom
"""
import psutil
from guizero import App, Text, ListBox, PushButton, Box, warn

def get_process_list():
    """Fetches a list of all running processes formatted for guizero."""
    processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            p_name = proc.info['name'] or 'Unknown'
            p_id = proc.info['pid']
            display_str = f"{p_name} (PID: {p_id})"
            processes.append((display_str, proc))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    # Sort processes alphabetically by display name
    processes.sort(key=lambda x: x[0].lower())
    return processes

def update_process_list():
    """Updates the ListBox with current running processes and builds the lookup map."""
    global process_dict
    process_list.clear()
    process_dict.clear()
    
    procs = get_process_list()
    for display_str, proc in procs:
        process_list.append(display_str)
        # Store process mapping by its unique string label
        process_dict[display_str] = proc

def get_selected_process():
    """Gets the currently selected process object using .value."""
    selected_value = process_list.value
    if selected_value and selected_value in process_dict:
        return process_dict[selected_value]
    return None

def terminate_process():
    """Gracefully requests a process to terminate."""
    proc = get_selected_process()
    if proc:
        try:
            proc.terminate()
            update_process_list()
        except Exception as e:
            warn("Error", f"Could not terminate process:\n{e}")
    else:
        warn("Selection Error", "Please select a process from the list first.")

def kill_process():
    """Forcefully kills a process."""
    proc = get_selected_process()
    if proc:
        try:
            proc.kill()
            update_process_list()
        except Exception as e:
            warn("Error", f"Could not kill process:\n{e}")
    else:
        warn("Selection Error", "Please select a process from the list first.")

# Initialize GUI with an expanded window size for larger text
app = App(title="Task Manager", width=500, height=600)

# Dictionary to map unique display strings directly to their psutil.Process objects
process_dict = {}

# Title & Description
instructions = Text(app, text="Select a process and choose an action:", size=14, )

# Process List Box (Enlarged text size set to 16)
process_list = ListBox(app, width=450, height=400)
process_list.text_size = 16
update_process_list()

# Action Buttons Container
button_box = Box(app, layout="grid")
btn_terminate = PushButton(button_box, command=terminate_process, text="Terminate (Soft)", grid=[0,0])
btn_kill = PushButton(button_box, command=kill_process, text="Kill (Force)", grid=[1,0], padx=10)

# Make the action button labels a bit bigger to match
btn_terminate.text_size = 12
btn_kill.text_size = 12

# Auto-refresh list every 5 seconds so it behaves like a task manager
app.repeat(5000, update_process_list)

# Start the application
app.display()
