import tkinter
from tkinter import messagebox

root=tkinter.Tk()
root.withdraw()

messagebox.showerror("Error","Error Message")
messagebox.showwarning("warning","warning Message")
messagebox.showwarning("Information","Informative message")
