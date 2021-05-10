import tkinter as tk
colours={'red','orange','yellow','green','blue','white'}

c=0
for x in colours:
    tk.Label(text=x,relief=tk.RIDGE,width=20).grid(row=c,column=0)
    tk.Entry(bg=x,relief=tk.SUNKEN,width=10).grid(row=c,column=1)
    c=c+1
tk.mainloop()
