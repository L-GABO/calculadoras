import tkinter as tk
from tkinter import filedialog
import subprocess

# List of Python scripts to include in the menu
import os

scripts = [
    os.path.join(os.getcwd(), "momento de inercia en perfiles", "momento de incercia en perfiles cuadrados huecos.py"),
    os.path.join(os.getcwd(), "tension", "tension de estres de pieza en estiramiento.py")
]

def open_script(script):
    # Open the selected script in a new window
    subprocess.Popen(["python", script])

def create_root_window():
    root = tk.Tk()
    root.title("Menu")
    return root

def create_buttons(root, scripts):
    for script in scripts:
        filename = os.path.splitext(os.path.basename(script))[0]
        button = tk.Button(root, text=filename, command=lambda script=script: open_script(script))
        button.pack()

def run_main_loop(root):
    root.mainloop()

def main():
    (lambda root: create_buttons(root, scripts) or root.mainloop())(create_root_window())

if __name__ == "__main__":
    main()