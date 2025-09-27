from tkinter import *

root = Tk()
root.title("Text Widget Example")
root.geometry("300x100")

text_widget = Text(root, height=3, width=30, font=("Arial", 12), bg="lightyellow")
text_widget.pack(padx=10, pady=10)

text_widget.insert(END, 'GeeksforGeeks\nBEST WEBSITE\n')
text_widget.config(state=DISABLED)

root.mainloop()
