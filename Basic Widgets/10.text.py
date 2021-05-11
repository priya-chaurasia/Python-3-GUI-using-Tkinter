import tkinter as tk

root=tk.Tk()

text=tk.Text(root,height=15,width=50)
text.pack()
text.insert(tk.END," This is python text widget \n This is python text widget \n")
tk.mainloop()