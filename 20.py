import tkinter as tk
root = tk.Tk()
root.title("Color Options in Tkinter")
root.geometry("300x150")
button = tk.Button(
    root,
    text="Click Me",
    activebackground="blue",
    activeforeground="white",
    width=20,
    height=2)
button.pack(pady=5)
label = tk.Label(
    root,
    text="Hello, Tkinter!",
    bg="lightgray",
    fg="black",
    font=("Arial", 12))
label.pack(pady=5)

entry = tk.Entry(root,selectbackground="lightblue",
    selectforeground="black", width=30)
entry.pack(pady=5)
root.mainloop()
