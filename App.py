import tkinter as tk
import subprocess
import time
import pygetwindow as gw

def devMode():
    subprocess.Popen(["C://Users//callu\AppData//Local//Programs//Microsoft VS Code//code.exe"])
    time.sleep(2)

    win = gw.getWindowsWithTitle("Welcome - Visual Studio Code")[0]
    win.maximize()
    
    subprocess.Popen(["C://Users//callu\AppData//Local//Programs//Microsoft VS Code//code.exe"])
    time.sleep(2)

    win = gw.getWindowsWithTitle("Welcome - Visual Studio Code")[0]
    win.maximize()

root = tk.Tk()
root.title("App Launcher")
root.geometry("600x400")

button = tk.Button(root, text="Dev", command=devMode)
button.pack()

root.mainloop()