"""
Created on Sun Jul 19 10:29:44 2026
this program is under the PolyForm Noncommercial License 10.0
@author: gemzoom
"""
import psutil
from guizero import App, Text, ListBox, PushButton, Box, warn

def get_process_list():
    """Fetches a list of running processes, sorts them by CPU usage, and formats for guizero."""
    processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            p_name = proc.info['name'] or 'Unknown'
            p_id = proc.info['pid']
            
            # Use interval=0.0 to get non-blocking CPU percentage
            cpu_usage = proc.cpu_percent(interval=0.0)
            
            display_str = f"{p_name} (PID: {p_id}) - CPU: {cpu_usage:.1f}%"
            processes.append((display_str, proc, cpu_usage))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass 
            
    # Sort processes by CPU usage (index 2) in descending order
    processes.sort(key=lambda x: x[2], reverse=True)
    return processes

def update_process_list():
    """Updates the ListBox while maintaining user scroll position and selection."""
    global process_dict
    
    # 1. Access the underlying Tkinter listbox widget inside guizero's Frame
    tk_listbox = None
    for child in process_list.tk.children.values():
        if child.__class__.__name__ == 'Listbox':
            tk_listbox = child
            break

    # 2. Save current selection and scroll position before clearing
    selected_value = process_list.value
    top_index = 0.0
    if tk_listbox:
        # yview() returns a tuple like (top_visible_fraction, bottom_visible_fraction)
        top_index = tk_listbox.yview()[0]
    
    process_list.clear()
    process_dict.clear()
    
    procs = get_process_list()
    for display_str, proc, _ in procs:
        process_list.append(display_str)
        process_dict[display_str] = proc

    # 3. Restore previous selection if it still exists in the new list
    if selected_value and selected_value in process_dict:
        process_list.value = selected_value
        
    # 4. Restore the scroll position so it doesn't jump back to the top
    if tk_listbox:
        tk_listbox.yview_moveto(top_index)

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
            warn('Error', f'Could not terminate process:\n{e}')
    else:
        warn('Selection Error', 'Please select a process from the list first.')

def kill_process():
    """Forcefully kills a process."""
    proc = get_selected_process()
    if proc:
        try:
            proc.kill()
            update_process_list()
        except Exception as e:
            warn('Error', f'Could not kill process:\n{e}')
    else:
        warn('Selection Error', 'Please select a process from the list first.')

# Initialize GUI with an expanded window size for larger text
app = App(title='Task Manager', width=600, height=600)

# Dictionary to map unique display strings directly to their psutil.Process objects
process_dict = {}

# Title & Description
instructions = Text(app, text='Select a process and choose an action:', size=14)

# Process List Box
process_list = ListBox(app, width=550, height=400)
process_list.text_size = 14
update_process_list()

# Action Buttons Container
button_box = Box(app, layout='grid')
btn_terminate = PushButton(button_box, command=terminate_process, text='Terminate (Soft)', grid=[0,0])
btn_kill = PushButton(button_box, command=kill_process, text='Kill (Force)', grid=[1,0], padx=10)

btn_terminate.text_size = 12
btn_kill.text_size = 12

# Auto-refresh list every 5 seconds
app.repeat(5000, update_process_list)

# Start the application
app.display()
