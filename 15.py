import tkinter as tk
from tkinter import ttk

def start_progress():
    progress['value'] = 0
    update_progress(0)

def update_progress(value):
    if value <= 100:
        progress['value'] = value
        root.after(50, update_progress, value + 1)  # Schedule the next update
    else:
        progress.stop()

root = tk.Tk()
root.title("Progressbar Example")
root.geometry("400x150")
progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=20)
start_button = tk.Button(root, text="Start Progress", command=start_progress)
start_button.pack(pady=10)
root.mainloop()
