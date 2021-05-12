from tkinter import*
from tkinter import ttk
app=Tk()
progb=ttk.Progressbar(app,orient=HORIZONTAL,length=200)
progb.pack()
progb.config(mode='indeterminate')
progb.start()
progb.stop()
progb.config(mode='determinate',maximum=15.0,value=6.2)
progb.config(value=9.0)
value=DoubleVar()
progb.config(variable=value)
scale=ttk.Scale(app,orient=HORIZONTAL,length=500,variable=value,from_=0.0, to =15.0)
scale.pack()
scale.set(4.2)
app.mainloop()