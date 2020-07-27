from tkinter import *

def job(event):
    print(event.x)

root=Tk()
root.geometry("500x300")
root.title("Events")
button=Button(text="Click me!")
button.pack()
button.bind('<Button-1>',job)
button.bind('<Double-1>',quit)

root.mainloop()