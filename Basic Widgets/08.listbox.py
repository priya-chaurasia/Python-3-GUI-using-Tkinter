from tkinter import *

root=Tk()
root.geometry("400x400")
lbl=Label(root, text="This is the list of programming languages")
listbox=Listbox(root)
listbox.insert(1,"Python")
listbox.insert(2,"Java")
listbox.insert(3,"C++")
listbox.insert(4,"C")

btn=Button(root, text="Delete",command= lambda listbox=listbox: listbox.delete(ANCHOR))
lbl.pack()
listbox.pack()
btn.pack()
root.mainloop()
