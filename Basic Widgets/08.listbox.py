from tkinter import *

root=Tk()
root.geometry("400x400")
lbl=Label(root, text="this is list programming languages")
listbox=Listbox(root)
listbox.insert(1,"python")
listbox.insert(2,"Java")
listbox.insert(3,"C++")
listbox.insert(4,"Ruby")

btn=Button(root, text="delete",command= lambda listbox=listbox: listbox.delete(ANCHOR))
lbl.pack()
listbox.pack()
btn.pack()
root.mainloop()