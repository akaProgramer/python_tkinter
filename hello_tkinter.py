from tkinter import *

mahmudul_root = Tk()

mahmudul_root.geometry("1255x944")
photo = PhotoImage(file="baby_lol.png")

# For Jpg Images

# image = Image.open("lol.JPG")
# photo = ImageTk.PhotoImage(image)

varun_label = Label(image=photo)
varun_label.pack()

mahmudul_root.mainloop()