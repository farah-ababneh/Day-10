from tkinter import *
root = Tk()
root.title("Spinbox Example")
root.geometry("250x150")
Label(root, text="Select a number:").pack(pady=5)
spinbox = Spinbox(root, from_=0, to=10, font=("Arial", 12), width=10)
spinbox.pack(pady=5)
def show_value():
    print("Selected value:", spinbox.get())

Button(root, text="Get Value", command=show_value).pack(pady=10)
root.mainloop()
