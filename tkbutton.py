from tkinter import *
def print_message():
    print("hello TKINter")
root= Tk()
root.geometry("500x600")
f1 = Frame(root , borderwidth = 2, bg ="grey" ,relief= RAISED)
f1.pack()

button2 = Button(f1, bg="grey", text="button", fg="white", command=print_message)
button2.pack()

button3 = Button(f1, bg="grey", text="button", fg="white")
button3.pack()

button4 = Button( bg="grey", text="button", fg="white")
button4.pack(side = LEFT)

button5 = Button(f1, bg="grey", text="button", fg="white")
button5.pack(side = RIGHT)

root.mainloop()