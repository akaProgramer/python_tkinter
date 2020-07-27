from tkinter import *
from PIL import Image,ImageTk

def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text +=text[i]
        if i%100==0 and i!=0:
            final_text += "\n"
    return final_text

root= Tk()
root.geometry("900x800")
root.title("Newspaper")


Newspaper_name = Label(root,text = "Hindustan Times", font = ("algerian", 50,"underline"), borderwidth = 4, relief = GROOVE, padx = 30, pady = 20, bg="#C2B280")
Newspaper_name.pack()

texts= []
photos= []
for i in range(0,3):
    with open(f"{i+1}.txt") as f:
        text= f.read()
        texts.append(every_100(text))
    image= Image.open(f"{i+1}.png")
    #resize images
    image = image.resize((100, 100), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))

f1= Frame(root, width=900, height=200, padx=31)
Label(f1,text=texts[0],pady= 22).pack(side="left")
Label(f1, image=photos[0], anchor="e").pack()
f1.pack(anchor="w")

f2= Frame(root, width=900, height=200, padx=31)
Label(f2,text=texts[1],pady= 22).pack(side="right")
Label(f2, image=photos[1], anchor="e").pack()
f2.pack(anchor="w")

f3= Frame(root, width=900, height=200, padx=31)
Label(f3,text=texts[2],pady= 22).pack(side="left")
Label(f3, image=photos[2], anchor="e").pack()
f3.pack(anchor="w")
root.mainloop()

f4= Frame(root, width=900, height=200, padx=31)
Label(f4,text=texts[3],pady= 22).pack(side="right")
Label(f4, image=photos[3], anchor="e").pack()
f4.pack(anchor="w")
root.mainloop()