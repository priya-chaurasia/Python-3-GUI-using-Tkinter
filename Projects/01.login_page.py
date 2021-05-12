from tkinter import *
import os
creds='credss.temp'
def signup():
    global passwords
    global nameL
    global roots

    roots=Tk()
    roots.title('Sign up')
    instructs=Label(roots,text='Please enter the user name and password\n')
    instructs.grid(row=0,column=0,sticky=E)
    nameL=Label(roots,text='User Name')
    passwords=Label(roots,text='Password')
    nameL.grid(row=1,column=0,sticky=W)
    passwords.grid(row=2,column=0,sticky=W)

    nameL=Entry(roots)
    passwords=Entry(roots,show='*')
    nameL.grid(row=1,column=1)
    passwords.grid(row=2,column=1)

    signupBtn=Button(roots,text='Sign up',command=Fsignup)
    signupBtn.grid(columnspan=2,sticky=W)
    roots.mainloop()

def Fsignup():
    with open(creds,'w') as f:
        f.write(nameL.get())
        f.write('\n')
        f.write(passwords.get())
        f.close()
    roots.destroy()
    login()

def login():
    global  nameLL
    global passwordL
    global roota

    roota=Tk()
    roota.title('Login')
    instructs=Label(roota,text='Login\n')
    instructs.grid(sticky=E)
    nameLL=Label(roota,text='Please enter the username')
    passwordL=Label(roota,text='Please enter the password')
    nameLL.grid(row=1,sticky=W)
    passwordL.grid(row=2,sticky=W)

    nameLL=Entry(roota)
    passwordL=Entry(roota,show='*')
    nameLL.grid(row=1,column=1)
    passwordL.grid(row=2,column=1)

    loginbtn=Button(roota,text='Login',command=CheckLogin)
    loginbtn.grid(column=2,sticky=W)


    usera=Button(roota,text='Delete user',fg="blue",command=Deluser)
    usera.grid(columnspan=2,sticky=W)
    roota.mainloop()



def CheckLogin():
    with open(creds) as f:
        data=f.readlines()
        uname=data[0].rstrip()
        passwod=data[1].rstrip()

    if nameLL.get()==uname and passwordL.get()==passwod:
        r=Tk()
        r.title(' Login page ')
        r.geometry('400x400')
        rlbl=Label(r,text='\n[+] logged In')
        rlbl.pack()
        r.mainloop()
    else:
        r=Tk()
        r.title("Login Checked")
        r.geometry('400x400')
        rlbl = Label(r, text='\n[+] Invalid login ID or Password')
        rlbl.pack()
        r.mainloop()


def Deluser():
    os.remove(creds)
    roota.destroy()
    signup()
if os.path.isfile(creds):
    login()
else:
    signup()
