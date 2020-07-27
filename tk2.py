from tkinter import *

root = Tk()
root.geometry("600x500")
root.title("My GUI")

# important label option
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"

# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE


text_label = Label(text = '''my name is ravi but on discord people call me bazooka.
I like talk with random people on discord. 
I have met many people on that platform there are many types
of people for eg:- toxic, people who like to have a peaeful conversation'''
,bg="orange",fg="white", padx=121 , pady=32 , font = ("wide latin",12,"italic"), borderwidth = 5 , relief = SUNKEN)


# Important Pack options
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady

# title_label.pack(side=BOTTOM, anchor ="sw", fill=X)
text_label.pack(anchor = "nw" , side = LEFT, fill = X)
root.mainloop()