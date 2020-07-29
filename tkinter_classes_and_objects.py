from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x400")
    
    def status(self):
        self.var= StringVar()
        self.var.set("Ready")
        self.statusbar= Label(self, textvar=self.var, relief= SUNKEN)
        self.statusbar.pack(fill=X)
    def  click(self):
        print("Clicked")
    def createButton(self):
        Button(text="click me", command=self.click).pack()
        


if __name__ == "__main__":
    window= GUI()
    window.status()
    window.createButton()
    window.mainloop()