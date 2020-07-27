from tkinter import *
import tkinter.messagebox as tmsg

def hello():
    print("working")

def help():
    print("We are always there for helping dont take tension")
    tmsg.showinfo("Help:","Its gonna be great if we help u out")

def rate():
    print("Rate Us")
    value=tmsg.askquestion("Ratings","how was your experience good",)
    if value == "yes":
        msg= "We are Glad to know that, thanks for your feedback"
    else:
        msg= "Please tell us about your issue on acf@gmail.com, we'll try to reolve it"
    tmsg.showinfo("experience",msg)



root= Tk()
root.geometry("700x600")
root.title("Menu bars")

# # non dropdowm menu
# my_menu= Menu(root)
# my_menu.add_command(label="File", command=hello)
# my_menu.add_command(label= "Quit", command= quit)
# root.config(menu=my_menu)



mainmenu= Menu(root)
m1= Menu(mainmenu, tearoff=0)
m1.add_command(label="New File", command=hello)
m1.add_command(label="New Window.....", command=hello)
m1.add_separator()
m1.add_command(label="Open File", command=hello)
m1.add_command(label="Open Folder", command=hello)
m1.add_command(label="Open Workspace", command=hello)
m1.add_separator()
root.config(menu=mainmenu)

mainmenu.add_cascade(label="File", menu=m1)

m2= Menu(mainmenu, tearoff=0)
m2.add_command(label="Undo", command=hello)
m2.add_command(label="Redo", command=hello)
m2.add_separator()
m2.add_command(label="Cut", command=hello)
m2.add_command(label="Copy", command=hello)
m2.add_command(label="Paste", command=hello)
root.config(menu=mainmenu)

mainmenu.add_cascade(label="Edit", menu=m2)

m3= Menu(mainmenu, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate Us", command=rate)
m3.add_separator()
root.config(menu=mainmenu)

mainmenu.add_cascade(label="Help", menu=m3)

root.mainloop()