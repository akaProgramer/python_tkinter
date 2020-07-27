from tkinter import *
import tkinter.messagebox as tmsg

def getdollar():
    print("we got your request")
    tmsg.showinfo("Amount Credited",f"{myslider2.get()} amount is tarnsfered to your account")
    
root= Tk()
root.geometry("523x432")
root.title("Slider")

# myslider= Scale(root, from_=0, to=100)
# myslider.pack()
Label(root, text="How many dollars u want").pack(padx=23)

myslider2= Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50, length= 300)
# myslider2.set(23)
myslider2.pack()

Button(text="Get dollars",relief=RAISED, command=getdollar).pack(padx=23)

root.mainloop()