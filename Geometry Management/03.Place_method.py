from tkinter import *

root=Tk()

l1=Label(root,text="Maths")
l1.place(x=10,y=10)
e1=Entry(root,bd=5)
e1.place(x=60,y=10)

l2=Label(root,text="Bio")
l2.place(x=10,y=45)
e2=Entry(root,bd=4)
e2.place(x=60,y=45)

l3=Label(root,text="Total")
l3.place(x=10,y=150)
e3=Entry(root,bd=5)
e3.place(x=60,y=150)

b=Button(root,text="Add")
b.place(x=100,y=100)
root.geometry("250x250+10+10")
root.mainloop()
