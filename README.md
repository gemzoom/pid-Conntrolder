# Simple Python PID conntroller

A lightweight, cross-platform graphical Task Manager built with Python. It lists running system processes alphabetically and allows users to gracefully terminate or forcefully kill selected tasks. The interface auto-refreshes every 5 seconds to provide real-time updates.

## Features

*   **Process Overview:** Lists all active system processes with their names and Process IDs (PIDs).
*   **Alphabetical Sorting:** Automatically sorts the process list for easy navigation.
*   **Soft Termination:** Safely requests processes to close using `terminate()`.
*   **Force Kill:** Forcefully stops stubborn processes using `kill()`.
*   **Auto-Refresh:** Dynamically updates the process list every 5 seconds.
*   **Error Handling:** Displays clear GUI warning dialogs if a process cannot be closed due to access restrictions or system limits.

## Prerequisites

You need Python 3 installed on your system along with the following libraries:


*   **psutil:** Used for retrieving information on running processes and system utilization.
*   **guizero:** A wrapper around `tkinter` designed to make creating simple graphical user interfaces quick and easy.

You can install these libs with the following command:
```bash
pip install psutil guizero
```

## How to Run

1. Clone or download the script file [here](https://github.com/gemzoom/pid-Conntrolder/blob/main/pid-Conntrolder.py).
2. Run the script using your terminal or command prompt:

```bash
python pid-Conntrolder.py
```

## How to Use

1. **Launch** the application to populate the process window.
2. **Scroll** through the cpu usage ordered list.
3. **Click** on a process name to select it.
4. **Choose an action** at the bottom of the interface:
    *   Click **Terminate (Soft)** to request a normal closure.
    *   Click **Kill (Force)** to instantly force the process to stop.

## License

This project is licensed under the **PolyForm Noncommercial License 1.0.0**. It is free to use, modify, and distribute for noncommercial purposes.

***

**Author:** gemzoom  
**Created:** July 19, 2026
