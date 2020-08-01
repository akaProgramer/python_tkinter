from tkinter import *

def uplaod():
    statusvar.set("Busy...")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready Now")
root= Tk()
root.geometry("600x300")
root.title("Status Bar")

statusvar= StringVar()
statusvar.set("Ready")
sbar= Label(root, textvariable=statusvar, relief=SUNKEN)
sbar.pack(side=BOTTOM, fill=X)
Button(root, text="Upload", command=uplaod).pack()
root.mainloop()