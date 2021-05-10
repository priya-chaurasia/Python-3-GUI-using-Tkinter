import tkinter as tk
root=tk.Tk()

tk.Label(root,text="Email Id").grid(row=0)
tk.Label(root,text="Password").grid(row=1)
a1=tk.Entry(root)
a2=tk.Entry(root)
a1.grid(row=0,column=1)
a2.grid(row=1,column=1)

root.mainloop()
