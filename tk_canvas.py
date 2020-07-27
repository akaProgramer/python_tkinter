from tkinter import *

root= Tk()
root.geometry("600x500")
canvas_height= 500   
canvas_width= 600
root.title("CANVAS")

canvas_area= Canvas(root, width= canvas_width, height=canvas_height, bg="skyblue")
canvas_area.pack()
canvas_area.create_rectangle(111,111,333,333,fill= "orange")


root.mainloop()