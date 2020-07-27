from tkinter import *

def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1

i=0
root= Tk()
root.geometry("500x300")
root.title("checkbox tutorial")

lbx=Listbox(root)
lbx.pack()
lbx.insert(END,"First Item of our Listbox")

Button(root, text="Add Item", command=add).pack()
root.mainloop()