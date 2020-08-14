from tkinter import *
from time import sleep
import re
#(-?\d+[.+\-*\/^%])*(\d+)
def key_check(inp):
    try:
        int(inp)
    except ValueError:
        return False
    else:
        return True
def key_pressed(event):
    text = value.get()
    print(text)
    value.set(value.get()[:-1])
    value_bar.update()
    if not key_check(text):
        value.set(re.sub("[a-zA-Z\[\]\(\)!@#$^&\?\{\}:,;\"\"\|'~`]", "", text))
# ⌫	
def pressButton(b): 
    b.invoke()
    b.config(relief="sunken",fg="white", bg="orange")
    root.after(100, lambda button=b: button.config(relief="groove",bg="white",fg="black"))

def correct(inp):
    global value
    try:
        if len(value.get())<=20 and (inp=="00" or inp=="0" or inp=="=" or inp=="C" or inp=="←" or inp=="." or inp=="+" or inp=="*" or inp=="-" or inp=="/" or inp=="**" or int(inp)):
            return True
        elif inp=="C" or inp=="←" or inp=="=":
            return True
    except:
        return False


def click(event,b):
    global value
    text= event.widget.cget("text")
    if correct(text):
        if text == "=":
            if value.get().isdigit():
                scvalue= int(value.get())  
            else:
                try:
                    scvalue= eval(value.get()) 
                    if len(str(scvalue))>20:
                        scvalue="Overflow"
                        value.set(scvalue)
                        value_bar.update()
                        sleep(0.5)
                        value.set("")
                    else:
                        value.set(scvalue)
                        value_bar.update()
                except:
                    scvalue= "Error"
                    value.set(scvalue)
                    value_bar.update()
                    sleep(0.5)
                    value.set("")
        elif text== "C":
            value.set("")
            value_bar.update()
        elif text=="←":
            value.set(value.get()[:-1])
            value_bar.update()
        else:
            if value.get()=="0":
                value.set(value.get()[:-1])
            value.set(value.get()+str(text))
            print(value.get())
            syntax= re.compile(r"(-?\d+[.+\-*\/^%])*(\d+)")
            result= syntax.match(value.get())
            value.set(result.group())
            value_bar.update()
    else:
        value.set(value.get()+str(""))
        value_bar.update()
        

def entered(event,b):
    b.config(bg="#caced9",fg="#f2f4fa")
def left(event,b):
    b.config(bg="white", fg="black")
root= Tk()

root.geometry("600x650")
root.title("Calculator")
value= StringVar()
value.set("0")
signs = ["+","-","*","C","/","←","**","="]
add_signs=[".","0","00"]
k=0
value_bar= Entry(root, textvar=value, font="sans-serif 30 bold",relief=SUNKEN,borderwidth=10)
value_bar.pack(pady=20, padx=10,ipady=13,fill=X)
value_bar.focus_set() 
b_frame= Frame(root)
b_frame.pack(side= TOP,fill=BOTH,padx=10,pady=20,expand=True)
root.bind("<Key>",lambda event: key_pressed(event))
#num_buttons
for i in range(1,5):
    Grid.rowconfigure(b_frame,i,weight=1)
    for j in range(0,3):
        if i<=3:
            bj= Button(b_frame, text=f"{10-(3*i)+j}",relief=GROOVE, font="sans-serif 20 bold",border="2px black", fg="black", bg="white",activebackground="white",width=4)
            root.bind(f"{10-(3*i)+j}", lambda e, b=bj: pressButton(b))
        else:
            bj= Button(b_frame, text=f"{add_signs[k]}",relief=GROOVE, font="sans-serif 20 bold",border="2px black", fg="black", bg="white",activebackground="white",width=4)
            root.bind(f"{add_signs[k]}", lambda e, b=bj: pressButton(b))
            k+=1
        bj.bind("<Enter>",lambda event, b=bj : entered(event,b))
        bj.bind("<Leave>",lambda event, b=bj : left(event,b))
        bj.bind("<Button-1>",lambda event, b=bj : click(event,b))
        Grid.columnconfigure(b_frame,j,weight=1)
        bj.grid(row=i,column=j,sticky=N+S+S+E+W)
#sign_buttons
for (i,sign) in zip(range(8),signs):
    if i>2:
        b_sign_i= Button(b_frame, text=f"{sign}",relief=GROOVE, font="sans-serif 20 bold",border="2px black", fg="black", bg="white",activebackground="white",width=15)
        if sign=="←":
            root.bind("<BackSpace>", lambda e, b=b_sign_i: pressButton(b))
        elif sign=="=":
            root.bind("<Return>", lambda e, b=b_sign_i: pressButton(b))
            root.bind("<=>", lambda e, b=b_sign_i: pressButton(b))
        elif sign=="C":
            root.bind("<Delete>", lambda e, b=b_sign_i: pressButton(b))
        else:
            root.bind(sign, lambda e, b=b_sign_i: pressButton(b))
        Grid.rowconfigure(b_frame,i-3,weight=1)
        Grid.columnconfigure(b_frame,4,weight=1)
        b_sign_i.grid(row=i-3,column=4,sticky=N+S+S+E+W)   
    else:
        b_sign_i= Button(b_frame, text=f"{sign}",relief=GROOVE, font="sans-serif 20 bold",border="2px black", fg="black", bg="white",activebackground="white",width=4)
        root.bind(sign, lambda e, b=b_sign_i: pressButton(b))
        Grid.rowconfigure(b_frame,0,weight=1)
        Grid.columnconfigure(b_frame,i,weight=1) 
        b_sign_i.grid(row=0,column=i,sticky=N+S+S+E+W)
    b_sign_i.bind("<Enter>",lambda event, b=b_sign_i : entered(event,b))
    b_sign_i.bind("<Leave>",lambda event, b=b_sign_i : left(event,b))
    b_sign_i.bind("<Button-1>",lambda event, b=b_sign_i : click(event,b))   
root.mainloop()