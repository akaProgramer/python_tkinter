from tkinter import *

root= Tk()
root.geometry("700x600")
root.title("Scroll Bar")

scrollbar= Scrollbar(root)
scrollbar.pack(side= RIGHT, fill=Y)
list_box= Listbox(root, yscrollcommand= scrollbar.set)
for i in range(300):
    list_box.insert(END,f"Item {i}")

list_box.pack(fill=BOTH)
scrollbar.config(command= list_box.yview)

root.mainloop()