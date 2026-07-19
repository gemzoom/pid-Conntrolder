Simple Python pid conntroller
lightweight, cross-platform graphical Task Manager built with Python. It lists running
system processes alphabetically and allows users to gracefully terminate or forcefully
kill selected tasks. The interface auto-refreshes every 5 seconds to provide real-time
updates.

FeaturesProcess Overview: Lists all active system processes with their names and Process IDs (PIDs).
Alphabetical Sorting: Automatically sorts the process list for easy navigation.
Soft Termination: Safely requests processes to close using terminate().
Force Kill: Forcefully stops stubborn processes using kill().
Auto-Refresh: Dynamically updates the process list every 5 seconds.
Error Handling: Displays clear GUI warning dialogs if a process cannot be closed due to access restrictions or system limits.
PrerequisitesYou need Python 3 installed on your system along with the following libraries:bashpip install psutil guizero.
psutil: Used for retrieving information on running processes and system utilization.
guizero: A wrapper around tkinter designed to make creating simple graphical user interfaces quick and easy.
How to RunClone or download the script file (e.g., task_manager.py).Run the script using your terminal or command prompt:bashpython task_manager.py
How to UseLaunch the application to populate the process window.Scroll through the alphabetically ordered list.
Click on a process name to select it.
Choose an action at the bottom of the interface:Click Terminate (Soft) to request a normal closure.Click Kill (Force) to instantly force the process to stop.
LicenseThis project is licensed under the PolyForm Noncommercial License 1.0.0. It is free to use, modify, and distribute for noncommercial purposes.Author: gemzoomCreated: July 19, 2026
