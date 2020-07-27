from tkinter import *

root = Tk()
root.geometry("500x600")
f1 = Frame (root, bg="yellow", borderwidth = 6 ,relief= GROOVE)

f1.pack(side=LEFT, fill=Y)
l = Label( f1,text = "project tkinter - pycharm" , pady=12)
l.pack(pady= 300)

f2 = Frame(root, bg="yellow" ,borderwidth = 6 , relief=GROOVE)
f2.pack(side = TOP, fill= X)
l = Label(f2, text ="Address of file", padx=4, font = "algerian 16 bold")
l.pack(padx = 50)
root.mainloop()