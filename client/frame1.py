from Tkinter import *

root = Tk()
var = StringVar()
var.set('hello')

l = Label(root, textvariable = var)
l.pack()

t = Entry(root, textvariable = var)
t.pack()

root.mainloop()
