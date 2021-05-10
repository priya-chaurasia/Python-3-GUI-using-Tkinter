import tkinter as tk

app=tk.Tk()
app.geometry("400x400")
radiovalue=tk.IntVar()
radio1=tk.Radiobutton(app,text='Januray',variable=radiovalue,value=1)
radio2=tk.Radiobutton(app,text='Feb',variable=radiovalue,value=2)
radio3=tk.Radiobutton(app,text='March',variable=radiovalue,value=3)
radio4=tk.Radiobutton(app,text='April',variable=radiovalue,value=4)


radio1.grid(column=0,row=0)
radio2.grid(column=0,row=1)
radio3.grid(column=0,row=2)
radio4.grid(column=0,row=3)

app.mainloop()
