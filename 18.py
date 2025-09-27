from tkinter import *

root = Tk()
root.title("Canvas Line Example")

canvas_width = 200
canvas_height = 60

canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack(padx=10, pady=10)

y = canvas_height // 2
canvas.create_line(0, y, canvas_width, y, fill="blue", width=3)

root.mainloop()
