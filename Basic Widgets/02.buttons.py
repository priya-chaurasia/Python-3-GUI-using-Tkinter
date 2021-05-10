'''import tkinter as tk
def slogan():
    print(("tkinter button"))

root=tk.Tk()
button=tk.Button(root,text="Quit",fg="red",command=quit)

button.pack(side=tk.LEFT)
slogan1=tk.Button(root,text="hello",command="slogan")
slogan1.pack(side=tk.LEFT)
root.mainloop()
'''

import tkinter as tk
counter=0
def count(label):
    counter=0
    def count1():
        global counter
        counter +=1
        label.config(text=str(counter))
        label.after(100,count1)
    count1()
root=tk.Tk()
root.title("counting secounds")
label=tk.Label(root,fg="blue")
label.pack()
count(label)
button=tk.Button(root,text="stop",width=25,command=root.destroy)
button.pack()
root.mainloop()

