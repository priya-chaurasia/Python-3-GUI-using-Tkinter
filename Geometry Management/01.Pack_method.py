import tkinter as tk

root=tk.Tk()
a=tk.Label(root,text=" Python",bg="blue",fg="white")
a.pack(fill=tk.X,padx=10,side=tk.LEFT)

a=tk.Label(root,text=" C",bg="red",fg="white")
a.pack(fill=tk.X,padx=5,side=tk.LEFT)

a=tk.Label(root,text=" C++",bg="green",fg="white")
a.pack(fill=tk.X,padx=2,side=tk.LEFT)

a=tk.Label(root,text=" Java",bg="yellow",fg="white")
a.pack(fill=tk.X,padx=1,side=tk.LEFT)


tk.mainloop()
