import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

# Get absolute paths to terminal and GUI scripts
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
TERMINAL_SCRIPT = os.path.join(PROJECT_DIR, "main.py")
GUI_SCRIPT = os.path.join(PROJECT_DIR, "gui.py")

# --- Functions ---
def run_terminal():
    try:
        # Open terminal version in a new console
        if sys.platform == "win32":
            subprocess.Popen(["python", TERMINAL_SCRIPT], creationflags=subprocess.CREATE_NEW_CONSOLE)
        else:
            subprocess.Popen(["python3", TERMINAL_SCRIPT])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run terminal version:\n{e}")

def run_gui():
    try:
        # Run GUI version
        import gui
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run GUI version:\n{e}")

# --- GUI ---
root = tk.Tk()
root.title("Secure Password Manager Launcher")
root.geometry("350x150")

tk.Label(root, text="Choose Version to Launch:", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="Terminal Version", command=run_terminal, width=25, height=2).pack(pady=5)
tk.Button(root, text="GUI Version", command=run_gui, width=25, height=2).pack(pady=5)

root.mainloop()
