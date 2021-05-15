from tkinter import *
root=Tk()
root.geometry('600x600')
root.title('Registration form')


label1=Label(root,text="Registraton Form",width=25,font=("bold",20))
label1.place(x=90,y=53)
label2=Label(root,text="Full Name",width=20,font=("bold",10))
label2.place(x=80,y=130)
entry1=Entry(root)
entry1.place(x=240,y=130)

label3=Label(root,text="Email",width=20,font=("bold",10))
label3.place(x=68,y=180)
entry2=Entry(root)
entry2.place(x=240,y=180)


label4=Label(root,text="Gender",width=20,font=("bold",10))
label4.place(x=70,y=230)
var=IntVar()
Radiobutton(root,text="Male",padx=5,variable=var,value=1).place(x=235,y=230)
Radiobutton(root,text="Female",padx=20,variable=var,value=2).place(x=290,y=230)

label5=Label(root,text="Country",width=20,font=("bold",10))
label5.place(x=70,y=280)

list1=['Canada','USA','Brazil','Australia','UK','Germany','Turkey'];
c=StringVar()
droplist=OptionMenu(root,c,*list1)
droplist.config(width=15)
c.set('Select Your country')
droplist.place(x=240,y=280)

label6=Label(root,text="Programming Languages",width=20,font=("bold",10))
label6.place(x=85,y=330)
var1=IntVar()
Checkbutton(root,text="Python",variable=var1).place(x=235,y=330)
Checkbutton(root,text="Java",variable=var1).place(x=290,y=380)
Checkbutton(root,text="C++",variable=var1).place(x=330,y=420)
Checkbutton(root,text="PHP",variable=var1).place(x=350,y=480)
Button(root,text='Submit',width=20,bg='red',fg='white').place(x=390,y=500)
root.mainloop()
