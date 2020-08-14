# import tkinter as tk
# root = tk. Tk()
# def key_pressed (event) :
#     print (event.char)


# root. bind ("<Key>", key_pressed)
# root . mainloop ()


# import tkinter as tk

# root = tk.Tk()

# def key(event):
#     print(repr(event.char), repr(event.keysym), repr(event.keycode))
# b1=tk.Button(root,text="1")
# b1.pack()

# b1.bind("<Key>", key)
# root.mainloop()
# from tkinter import *
# class MyClass:
#     def __init__(self, master):
#        frame = Frame(master)
#        frame.pack()

#        self.button = Button(frame, text="Hello", command=self.func)
#        self.button.pack(side='left')

#        master.bind('f', self.func)

#     def func(self, _event=None):
#         print("Hello, world")

# root = Tk()
# abc = MyClass(root)
# root.mainloop()
# from tkinter import Tk,Button

# root=Tk()

# for i in range(1,3):
#     bi= Button(text=i, width=5)
#     bi.pack(padx=10)


# root.mainloop()
# from tkinter import Tk,Button

# root=Tk()

# for i in range(1,3):
#     bi= Button(text=i, width=5, command=lambda number=i: print(f"My number is {number}"))
#     bi.pack(padx=10)
#     root.bind(i, lambda e, button=bi: button.invoke())

# root.mainloop()
# from tkinter import Tk,Button,Frame

# root=Tk()

# def pressButton(button):
#     button.invoke()
#     button.config(relief="sunken")
#     f.after(100, lambda button=button: button.config(relief="raised"))
# f= Frame(root)
# f.pack()
# i=0
# for j in range(3):
#     for i in range(1,5):
#         bi = Button(f,text=f"{k}", width=5, command=lambda number=i: print(f"My number is {number}"))
#         bi.pack(padx=10)
#         f.bind(i, lambda e, button=bi: pressButton(button))

# root.mainloop()


# from tkinter import Tk,Button,Entry,StringVar

# def check(inp):
#     try:
#         int(inp)
#         return True
#     except:
#         return False
# def click(event,b):
#     global var
#     text= event.widget.cget("text")
    
#     if check(text):
#         var.set(var.get()+str(text))
#     else:
#         var.set(var.get()+str(""))
#     entry.update()

        
# root=Tk()
# root.geometry("400x400")
# var=StringVar()
# entry= Entry(root,textvar=var)
# entry.pack()
# for i in range(1,5):
#     bi= Button(text=i, width=5)
#     bi.pack(padx=10,pady=10)
#     bi.bind("<Button-1>",lambda event, b=bi : click(event,b)) 
#     bi.bind("<Key>",lambda event, b=bi : click(event,b))
# b=Button(text="I",width=5)
# b.pack()
# b.bind("<Button-1>",lambda event, button=b : click(event,b)) 
# b.bind("<Key>",lambda event, buton=b : click(event,b))
# root.mainloop()
# from tkinter import *

# def get_info():
#     print(e.index(INSERT))

# root = Tk()
# e = Entry(root)
# e.pack()
# Button(root, text="get info", command=get_info).pack()
# root.mainloop()

from tkinter import *
root=Tk()

def correct(inp):
    if inp.isalpha():
        print(inp)
        return True
    elif inp is "":
        print(inp)
        return True
    else:
        print(inp)
        return False

e=Entry(root)
e.place(x=50,y=50)
reg=root.register(correct)
e.config(validate="key",validatecommand=(reg,'%P'))

root.mainloop()