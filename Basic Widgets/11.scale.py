from tkinter import *
def scl():
    selection=f"volume:{str(var.get())}"
    label.config(text=selection)


root=Tk()
var=DoubleVar()
scale=Scale(root,variable=var)
scale.pack(anchor=CENTER)
button=Button(root,text="get scale value",command=scl)

button.pack(anchor=CENTER)
label=Label(root)
label.pack()


root.mainloop()