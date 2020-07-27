from tkinter import *

root = Tk()

root.geometry("900x800")
root.title("Newspaper")

Newspaper_name = Label(root,text = "Times of India", font = ("algerian", 50,"underline"), borderwidth = 4, relief = GROOVE, padx = 30, pady = 20, bg="#C2B280")
Newspaper_name.pack()
Newspaper_headlines = Label(root,text = "Today's Headlines", font = ("arial black",20))
Newspaper_headlines.pack(pady=40)
photo = PhotoImage(file="ambitabh.png")

ambitabh_image = Label(image = photo)
ambitabh_image.pack()

ambitabh_news = Label(root, text = '''Coronavirus LIVE Updates: In a tweet,
Abhishek Bachchan said that both have mild symptoms and 
requested everybody to stay calm and not panic''', font = ("calibiri", 10))
ambitabh_news.pack()

gold_photo = PhotoImage(file= "gold.png")
gold_image= Label(image = gold_photo)
gold_image.pack()

gold_news = Label(root, text = '''Kerala gold smuggling case: 
Two key accused including Swapna Suresh held in Bengaluru''', font = ("calibiri", 10))
gold_news.pack()
root.mainloop()