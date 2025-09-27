from tkinter import *
root = Tk()
root.title("Message Example")
root.geometry("300x150")
our_message = "This is our Message"
message_label = Message(root, text=our_message, bg='lightgreen', width=250, font=("Arial", 12))
message_label.pack(pady=20)
root.mainloop()
