import tkinter as tk

root = tk.Tk()
root.title("Grid Example")
root.geometry("250x100")  

label1 = tk.Label(root, text="Label 1", font=("Arial", 10), padx=10, pady=5)
label2 = tk.Label(root, text="Label 2", font=("Arial", 10), padx=10, pady=5)
label3 = tk.Label(root, text="Label 3", font=("Arial", 10), padx=10, pady=5)

label1.grid(row=0, column=0, sticky="w")
label2.grid(row=0, column=1, sticky="e")
label3.grid(row=1, column=0, columnspan=2, pady=(5, 0))

root.mainloop()
