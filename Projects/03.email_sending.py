from tkinter import*
from tkinter import ttk

import smtplib
import webbrowser

def sendemail():
    try:
        sender=acct.get()
        recepient=[reciv.get()]
        subject=sub.get()
        msg=msgbody.get('1.0','end')
        msgtosend="""\
        from:%s
        To:%s
        subject :%s
        %s
        """% (sender,recepient,subject,msg)
        mail=smtplib.SMTP('smtp.gmail.com',587)
        mail.starttls()
        mail.login(sender,passwd)
        mail.sendmail(sender,recepient,msgtosend)
        mail.close()
        ttk.Label(mainframe,text="email sent successfully").grid(column=4,row=9,sticky=W)
    except Exception as e:
        ttk.Label(mainframe, text=str(e)).grid(column=4, row=9, sticky=W)


def setup(event):
    webbrowser.open_new(r"https://www.gmail.com")

root=Tk()
root.title("send emial via gmail account")

mainframe=ttk.Frame(root,padding="4 4 13 13")
mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(0,weight=1)

acct=StringVar
passwd=StringVar
reciv=StringVar
sub=StringVar
msgbody=StringVar


lbl=Label(mainframe,text="go to gmail account",fg="blue",cursor="hand2")
lbl.grid(columnspan=2,column=3,row=0,sticky=W)
lbl.bind("<Button-1>",setup)

ttk.Label(mainframe,text="your Email acoount").grid(column=0,row=1,sticky=W)
acct_entry=ttk.Entry(mainframe,width=30,textvariable=acct)
acct_entry.grid(column=4,row=1,sticky=(W,E))


ttk.Label(mainframe,text="Your Password").grid(column=0,row=2,sticky=W)
passwd_entry=ttk.Entry(mainframe,show="*",width=30,textvariable=passwd)
passwd_entry.grid(column=4,row=2,sticky=(W,E))

ttk.Label(mainframe,text="Recipent Email Account ").grid(column=0,row=3,sticky=W)
reciv_entry=ttk.Entry(mainframe,width=30,textvariable=reciv)
reciv_entry.grid(column=4,row=3,sticky=(W,E))

ttk.Label(mainframe,text="Compose Email ").grid(column=0,row=5,sticky=W)
sub_entty=ttk.Entry(mainframe,width=30,textvariable=sub)
sub_entty.grid(column=4,row=6,sticky=(W,E))

ttk.Label(mainframe,text="Message body of  Email ").grid(column=0,row=7,sticky=W)
msg_entry=Text(mainframe,width=30,height=12)
msg_entry.grid(column=4,row=7,sticky=(W,E))

ttk.Button(mainframe,text="send Email ",command=sendemail).grid(column=4,row=8,sticky=E)
for child in mainframe.winfo_children(): child.grid_configure(padx=5,pady=5)
acct_entry.focus()
root.mainloop()