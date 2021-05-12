from tkinter import *
from tkinter import ttk

def short(action):
    print(action)

app=Tk()
app.bind('<Control-c>',lambda e:short('Copy'))
app.bind('<Control-v>',lambda e:short('Paste'))
app.bind('<Control-x>',lambda e:short('Cut'))

app.mainloop()