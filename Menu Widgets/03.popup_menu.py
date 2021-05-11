from tkinter import*

root=Tk()

w=Label(root,text="right click to show the result",width=50,height=25)
w.pack()

popup=Menu(root,tearoff=0)
popup.add_command(label="Pause")
popup.add_command(label="Copy")

popup.add_separator()

popup.add_command(label="Home")

def do_popup(event):
    try:
        popup.tk_popup(event.x_root,event.y_root,0)
    finally:
        popup.grab_release()
w.bind("<Button-3>",do_popup)
b=Button(root,text="quit",command=root.destroy)
b.pack()
mainloop()