from tkinter import *
root=Tk()
variable=StringVar(root)
variable.set("Select")

a=OptionMenu(root,variable,"A","B","C","D")
a.pack()
def ok():
    print("Value is ",variable.get)
    root.quit()

btn1=Button(root,text="Submit",command=ok)
btn1.pack()
mainloop()
