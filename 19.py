from tkinter import *

root = Tk()
root.title("PanedWindow Example")
root.geometry("400x200")

paned_horizontal = PanedWindow(root, orient=HORIZONTAL)
paned_horizontal.pack(fill=BOTH, expand=1, padx=10, pady=10)

left_entry = Entry(paned_horizontal, bd=5, width=20)
paned_horizontal.add(left_entry)

paned_vertical = PanedWindow(paned_horizontal, orient=VERTICAL)
paned_horizontal.add(paned_vertical)

top_scale = Scale(paned_vertical, orient=HORIZONTAL, length=150)
paned_vertical.add(top_scale)

root.mainloop()
