from tkinter import *

root = Tk()

def button1_message():
    print("hello from button 1")
def button2_message():
    print("hello from button 2")
def button3_message():
    print("hello from button 3")
def button4_message():
    print("hello from button 4")
def button1_message():
    print("hello from button 1")
root.geometry("445x423")
f1= Frame(root,bg="skyblue", borderwidth= 4, relief=RAISED)
f1.pack(side=TOP)

Button1 = Button(f1,text="button 1" , bg="orange" , fg="green", command=button1_message)
Button1.pack(padx= 5, side=LEFT)

Button2 = Button(f1,text="button 2" , bg="orange" , fg="green", command=button2_message)
Button2.pack(padx= 5, side=LEFT)

Button3 = Button(f1,text="button 3" , bg="orange" , fg="green", command=button3_message)
Button3.pack(padx= 5, side=LEFT)

Button4 = Button(f1,text="button 4" , bg="orange" , fg="green", command=button4_message)
Button4.pack(pady= 5, side=LEFT)

root.mainloop()