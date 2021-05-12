from tkinter import*
root=Tk()
root.title("mouse cursor")
root.geometry("500x500")

btn=Button(text="this is coursor example",relief=RAISED,cursor="circle").pack()
btn=Button(text="this is coursor example",relief=RAISED,cursor="clock").pack()
btn=Button(text="this is coursor example",relief=RAISED,cursor="star").pack()
btn=Button(text="this is coursor example",relief=RAISED,cursor="mouse").pack()
btn=Button(text="this is coursor example",relief=RAISED,cursor="man").pack()
btn=Button(text="this is coursor example",relief=RAISED,cursor="dotbox").pack()
btn=Button(text="this is coursor example",relief=RAISED,cursor="sizing").pack()
btn=Button(text="this is coursor example",relief=RAISED,cursor="plus").pack()
btn=Button(text="this is coursor example",relief=RAISED,cursor="heart").pack()





root.mainloop()