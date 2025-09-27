import tkinter as tk

root = tk.Tk()
root.title("Pack Example")
root.geometry("200x180")
button1 = tk.Button(root, text="Button 1", width=15, height=2, font=("Arial", 10))
button2 = tk.Button(root, text="Button 2", width=15, height=2, font=("Arial", 10))
button3 = tk.Button(root, text="Button 3", width=15, height=2, font=("Arial", 10))

button1.pack(pady=5)
button2.pack(pady=5)
button3.pack(pady=5)

root.mainloop()
