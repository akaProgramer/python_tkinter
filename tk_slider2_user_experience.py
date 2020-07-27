from tkinter import *
import tkinter.messagebox as tmsg

def get_review():
    with open("reviews.txt","a") as f:
        f.write(f"Name:- {user_name_value.get()}\nPhone no:- {Phone_no_value.get()}\nRatings:- {rating_slider.get()}\nName of dish:- {Name_of_dish_value.get()}\n\n")
    tmsg.showinfo("Rating","Your review has been recorded ,thanks for your feedback")

root= Tk()
root.geometry("500x450")
root.title("User experience")

Label(text="Rate our food service", padx=23, pady=23, bg="skyblue", font="arialblack 20").grid(pady=32,column=1,row=0)
user_name= Label(root, text="User name: ", font="palatino 12") 
Name_of_dish= Label(root,text="Name of Dish: ", font="palatino 12")
Phone_no= Label(root,text="Phone number: ", font="palatino 12")
user_name.grid(column=0, row=1, pady= 12,padx=10)
Phone_no.grid(column=0, row=2, pady= 12,padx=10)
Name_of_dish.grid(column=0, row=3, pady= 12,padx=10)

user_name_value= StringVar()
Phone_no_value= StringVar()
Name_of_dish_value= StringVar()

user_name_entry= Entry(root, textvariable= user_name_value)
phone_no_entry= Entry(root, textvariable= Phone_no_value)
Name_of_dish_entry= Entry(root, textvariable= Name_of_dish_value)
user_name_entry.grid(column=1, row=1, pady= 12)
phone_no_entry.grid(column=1, row=2, pady= 12)
Name_of_dish_entry.grid(column=1, row=3, pady= 12)

rating_slider= Scale(from_=1, to=5, tickinterval=1, orient=HORIZONTAL)
rating_slider.grid(pady=12,column=1)
Button(text="Send Review", bg="grey", command=get_review,fg="White", relief=RAISED, font="gramond 13").grid(column=1, row=7)
root.mainloop()