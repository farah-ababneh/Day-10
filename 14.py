from tkinter import *
top = Tk()
top.title("Menu Button Example")
top.geometry("200x100")
mb = Menubutton(top, text="GfG", relief=RAISED)
mb.pack(pady=20)
mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu
cVar = IntVar()
aVar = IntVar()
mb.menu.add_checkbutton(label='Contact', variable=cVar)
mb.menu.add_checkbutton(label='About', variable=aVar)
top.mainloop()
