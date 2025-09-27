import tkinter as tk

def on_key_press(event):
    print(f"[KEY]    You pressed: {event.keysym}")

def on_left_click(event):
    print(f"[CLICK]  Left click at ({event.x}, {event.y})")

def on_right_click(event):
    print(f"[CLICK]  Right click at ({event.x}, {event.y})")

def on_mouse_motion(event):
    print(f"[MOUSE]  Moved to ({event.x}, {event.y})")
root = tk.Tk()
root.title("Event Handling Example")
root.geometry("400x200")

label = tk.Label(root, text="Interact with this window:\nMove mouse, click, or press a key",
                 font=("Arial", 12), fg="blue", pady=20)
label.pack(expand=True)
root.bind("<KeyPress>", on_key_press)
root.bind("<Button-1>", on_left_click)
root.bind("<Button-3>", on_right_click)
root.bind("<Motion>", on_mouse_motion)

root.mainloop()
