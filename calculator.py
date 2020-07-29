from tkinter import *
from time import sleep




def click(event,b):
    global value
    text= event.widget.cget("text")
    if text == "=":
        if value.get().isdigit():
            scvalue= int(value.get())  
        else:
            try:
                scvalue= eval(value.get())
            except:
                scvalue= "Error"
                value_bar.update()
        value.set(scvalue)
        value_bar.update()
    elif text== "C":
        value.set("")
        value_bar.update()
    elif text=="←":
        value.set(value.get()[:-1])
    else:
        value.set(value.get()+str(text))
        value_bar.update()
   
        

def entered(event,b):
    b.config(bg="#caced9",fg="#f2f4fa")

def left(event,b):
    b.config(bg="white", fg="black")
root= Tk()

root.geometry("600x850")
value= StringVar()
value.set("")
sign = ["C","-","*","/","+","←","="]
k=0
value_bar= Entry(root, textvar=value, font="sans-serif 20 bold")
value_bar.pack(fill= X, pady=20, padx=20,ipady= 5)
for i in range(4):
    fi= Frame(root)
    for j in range(1,5):
        if j==4 or i>=3:
            bj= Button(fi, text=sign[k],relief=GROOVE, font="sans-serif 20 bold",border="2px black", fg="black", bg="white",activebackground="white",width=10)
            k+=1
        else:
            bj= Button(fi, text=f"{(6+j-2*i)-i}",relief=GROOVE, font="sans-serif 20 bold",border="2px black", fg="black", bg="white",activebackground="white",width=4)
        bj.pack(padx=1,pady=10,side="left")
        bj.bind("<Enter>",lambda event, b=bj : entered(event,b))
        bj.bind("<Leave>",lambda event, b=bj : left(event,b))
        bj.bind("<Button-1>",lambda event, b=bj : click(event,b))
        bj.pack()
    fi.pack(pady=0)


root.mainloop()