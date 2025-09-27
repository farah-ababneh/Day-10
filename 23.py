import tkinter as tk

root = tk.Tk()
root.title("Place Example")
root.geometry("200x150") 

label = tk.Label(root, text="Label", font=("Arial", 12), bg="lightgray", padx=10, pady=5)

label.place(x=50, y=50)

root.mainloop()
