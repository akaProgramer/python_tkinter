from tkinter import *
def getvals():
    print("username:-",user_value.get())
    print("password:-",pass_value.get())

root= Tk()
root.geometry("333x555")
# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar
user_name =Label(root, text="User name") 
password =Label(root, text="Password") 
user_name.grid()
password.grid()
user_value= StringVar()
pass_value= StringVar()
user_entry= Entry(root, textvariable= user_value)
pass_entry= Entry(root, textvariable= pass_value)
user_entry.grid(row= 0, column= 1)
pass_entry.grid(row= 1, column= 1)
submit_button= Button(text="SUMBIT",command=getvals).grid()

root.mainloop()