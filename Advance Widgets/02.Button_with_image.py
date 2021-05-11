from tkinter import *
from tkinter.ttk import *

app=Tk()
Label(app,text="python image button",font=('Verdana',15)).pack(side=TOP,pady=10)
photo=PhotoImage(file="download.png")
Photoimage=photo.subsample(4,4)
Button(app,text="Click Me",image=Photoimage,compound=LEFT).pack(side=TOP)
mainloop()