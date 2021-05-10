'''import tkinter as tk
root=tk.Tk()
a=tk.Label(root,text="hello tkinter")
a.pack()
root.mainloop()
'''

from tkinter import *
root=Tk()
var=StringVar()
label=Label(root,textvariable=var,relief=RAISED)
var.set("Hey I am tkinter label")
label.pack()
root.mainloop()

