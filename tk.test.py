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

# from tkinter import *
# root=Tk()

# def correct(inp):
#     if inp.isalpha():
#         print(inp)
#         return True
#     elif inp is "":
#         print(inp)
#         return True
#     else:
#         print(inp)
#         return False

# e=Entry(root)
# e.place(x=50,y=50)
# reg=root.register(correct)
# e.config(validate="key",validatecommand=(reg,'%P'))

# root.mainloop()


import tkinter as Tk, re




class TransparentWin (Tk.Tk) :
    ''' Transparent Tk Window Class '''

    def __init__ (self) :

        Tk.Tk.__init__(self)

        self.Drag = Drag(self)

        ''' Sets focus to the window. '''
        self.focus_force()

        ''' Removes the native window boarder. '''
        # self.overrideredirect(True)

        ''' Disables resizing of the widget.  '''
        self.resizable(False, False)

        ''' Places window above all other windows in the window stack. '''
        self.wm_attributes("-topmost", True)

        ''' This changes the alpha value (How transparent the window should
            be). It ranges from 0.0 (completely transparent) to 1.0
            (completely opaque).  '''
        self.attributes("-alpha", 0.7)

        ''' The windows overall position on the screen  '''
        self.wm_geometry('+' + str(439) + '+' + str(172))

        ''' Changes the window's color. '''
        bg = '#3e4134'

        self.config(bg=bg)

        self.Frame = Tk.Frame(self, bg=bg)
        self.Frame.pack()

        ''' Exits the application when the window is right clicked. '''
        self.Frame.bind('<Button-3>', self.exit)

        ''' Changes the window's size indirectly. '''
        self.Frame.configure(width=162, height=100)

    def exit (self, event) :
        self.destroy()

    def position (self) :

        _filter = re.compile(r"(\d+)?x?(\d+)?([+-])(\d+)([+-])(\d+)")

        pos = self.winfo_geometry()

        filtered = _filter.search(pos)
        self.X = int(filtered.group(4))
        self.Y = int(filtered.group(6))

        return self.X, self.Y

class Drag:
    ''' Makes a window dragable. '''

    def __init__ (self, par, dissable=None, releasecmd=None) :

        self.Par        = par
        self.Dissable   = dissable

        self.ReleaseCMD = releasecmd

        self.Par.bind('<Button-1>', self.relative_position)
        self.Par.bind('<ButtonRelease-1>', self.drag_unbind)


    def relative_position (self, event) :

        cx, cy = self.Par.winfo_pointerxy()
        x, y = self.Par.position()

        self.OriX = x
        self.OriY = y

        self.RelX = cx - x
        self.RelY = cy - y

        self.Par.bind('<Motion>', self.drag_wid)

    def drag_wid (self, event) :

        cx, cy = self.Par.winfo_pointerxy()

        d = self.Dissable

        if d == 'x' :
            x = self.OriX
            y = cy - self.RelY
        elif d == 'y' :
            x = cx - self.RelX
            y = self.OriY
        else:
            x = cx - self.RelX
            y = cy - self.RelY

        if x < 0 :
            x = 0

        if y < 0 :
            y = 0

        self.Par.wm_geometry('+' + str(x) + '+' + str(y))

    def drag_unbind (self, event) :

        self.Par.unbind('<Motion>')

        if self.ReleaseCMD != None :
            self.ReleaseCMD()


    def dissable (self) :

        self.Par.unbind('<Button-1>')
        self.Par.unbind('<ButtonRelease-1>')
        self.Par.unbind('<Motion>')


def __run__ () :

    TransparentWin().mainloop()


if __name__ == '__main__' :

    __run__()