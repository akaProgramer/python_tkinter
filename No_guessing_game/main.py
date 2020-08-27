from tkinter import *
import tkinter.messagebox as tmsg
import random
import re
from PIL import Image,ImageTk

class number_guessing_game(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x700+400+50")
        # self.open_frame_content()
        self.game_frame_content()
        self.frame= None
        self.swap_frame(self.open_frame_content())
        self.attempt=0
        self.previous_guess=""
    def swap_frame(self,new_frame):
        if self.frame is not None:
            self.frame.destroy()
        self.frame= new_frame
        self.frame.pack(expand=True,fill=BOTH)
    
    def range_check(self):
        self.from_var= self.from_entry_var.get()
        self.to_var=self.to_entry_var.get()
        if (self.from_var>self.to_var) or (self.from_var=="") or (self.to_var=="") or (self.from_var=="" and self.to_var==""):
            self.output_display.config(text="range is not correct")
            self.from_entry.delete(0,END)
            self.to_entry.delete(0,END)
            self.from_entry.focus()
        elif int(self.to_var)-int(self.from_var)<7:
            self.output_display.config(text="range is too short")
            self.from_entry.delete(0,END)
            self.to_entry.delete(0,END)
            self.from_entry.focus()
        else:
            self.game_frame.config(bg="#6B5B95")
            self.random_number= random.randint(int(self.from_var),int(self.to_var))
            self.guess_number= re.sub('[0-9]','_',str(self.random_number))
            self.guess_number_space= " ".join(self.guess_number)
            self.display.config(text=self.guess_number_space)
            self.range_heading= Label(self.game_frame,text=f"range is from {self.from_var} to {self.to_var}",font="mssansserif 20 bold")
            self.range_heading.pack(pady=10,ipady=20,ipadx=10)
            self.range_frame.pack_forget()
            self.output_display.pack_forget()
            self.display.pack()
            self.user_input.pack(pady=30,ipady=10)
            self.check_button.pack(ipady=10,pady=40)
            self.heading.config(text="Guess the number if your can :)")
            self.previous_guesses.pack(pady=20)
            self.output_display.pack()

    def reset(self):
        value= tmsg.askquestion("Win","Wanna play it again!!")
        if value=="yes":
            self.attempt=0
            self.swap_frame(self.game_frame_content())
        if value=="no":
            self.swap_frame(self.open_frame_content())
    def check(self):
        self.attempt+=1
        user_number= self.user_input_var.get()
        random_number= self.random_number
        if self.user_input.get()=="":
            self.output_display.config(text="dont leave it empty")
            self.attempt-=1
        elif int(user_number)<int(self.from_var) or int(user_number)>int(self.to_var):
            self.output_display.config(text="Out of range",fg="red")
            self.user_input.delete(0,END)
        elif int(random_number)==int(user_number):
            self.output_display.config(text=f"Well done you guessed it correct in {self.attempt} attempts",fg="green")
            self.display.config(text=self.random_number)
            self.reset()
        elif int(user_number)<int(random_number):
            self.output_display.config(text="guess a higer number",fg="#cd5334")
            self.previous_guess+=user_number + " "  
            self.previous_guesses.config(text="pervious guesses:  "+str(self.previous_guess))
            self.user_input.delete(0,END)
        elif int(user_number)>int(random_number):
            self.output_display.config(text="guess a lower number",fg="grey")
            self.previous_guess+=user_number + " "  
            self.previous_guesses.config(text="pervious guesses:  "+str(self.previous_guess))
            self.user_input.delete(0,END)

    def correct(self,inp):
        if len(inp)>3:
            self.output_display.config(text="character limit is exceed")
            return False
        elif inp.isnumeric():
            self.output_display.config(text="")
            return True
        elif inp is "":
            return True
        else:
            self.output_display.config(text="Only numeric values are allowed")
            return False

    def open_frame_content(self):
        self.open_frame= Frame(self)
        self.open_frame.config(bg="#ffd700") 
        self.photo= Image.open("No_guessing_game/num.png")
        self.resize= self.photo.resize((600,400),Image.ANTIALIAS)
        self.resized_image= ImageTk.PhotoImage(self.resize)
        self.game_photo= Label(self.open_frame,image=self.resized_image,bd=10,relief=SUNKEN)  
        self.game_photo.pack(pady=10,expand=True)
        self.start_button= Button(self.open_frame,text="Start Game",bg="green",font="helvetica 40",cursor="hand2",command=lambda : self.swap_frame(self.game_frame_content()) )
        self.start_button.pack(pady=10,expand=True)
        return self.open_frame
    def range_frame_content(self):
        self.range_frame= Frame(self.game_frame,relief=SUNKEN,borderwidth=6)
        self.range_frame.config(bg="#ff6e4a")
        self.from_entry_var= StringVar()
        self.to_entry_var= StringVar()
        self.from_entry_label= Label(self.range_frame,text="From: ",font="mssensserif 20 bold",bg="#ff6e4a",fg="#ffffff")
        self.from_entry_label.grid(row=0,column=0,pady=10,padx=10)
        self.from_entry= Entry(self.range_frame,font="gothic 15 bold",textvar=self.from_entry_var)
        self.from_entry.grid(row=0,column=1,ipady=5,padx=10) 
        self.from_reg= self.game_frame.register(self.correct)
        self.from_entry.config(validate="key",validatecommand=(self.from_reg,'%P'))
        self.to_entry_label= Label(self.range_frame,text="To: ",font="mssensserif 20 bold",bg="#ff6e4a",fg="#ffffff")
        self.to_entry_label.grid(row=1,column=0,pady=10,padx=10)
        self.to_entry= Entry(self.range_frame,font="gothic 15 bold",textvar=self.to_entry_var)
        self.to_entry.grid(row=1,column=1,ipady=5) 
        self.to_reg= self.game_frame.register(self.correct)
        self.to_entry.config(validate="key",validatecommand=(self.to_reg,'%P'))
        self.submit_range= Button(self.range_frame,text="Submit Range",command=self.range_check,font="sensserif 20 bold",bg="yellow",fg="#ffffff",activebackground="#ffd59a",activeforeground="#ffffff",cursor="hand2")
        self.submit_range.grid(row=2,column=1,pady=40,padx=10,ipady=5,ipadx=20)
        self.range_frame.pack(pady=20)
        self.from_entry.focus()
        
    def game_frame_content(self):
        self.game_frame= Frame(self)
        self.game_frame.config(bg="#ff2052")
        self.heading= Label(self.game_frame,text="Give a range!!",font="times 40 bold underline",bg="#fffacd",fg="#1e90ff")
        self.heading.pack(pady=20,fill=X,ipady=10)
        self.range_frame_content()
        self.display= Label(self.game_frame,text="number",font="verdana 30")
        self.user_input_var= StringVar()
        self.user_input= Entry(self.game_frame,font="sensserif 30 bold",justify="center",textvar=self.user_input_var,width=5)
        self.reg= self.game_frame.register(self.correct)
        self.user_input.config(validate="key",validatecommand=(self.reg,'%P'))
        self.check_button= Button(self.game_frame,font="times 20",text="Check",relief=RAISED,bd=10,width=20,command=self.check)
        self.output_display= Label(self.game_frame,font="helvetica 25 bold")
        self.previous_guesses= Label(self.game_frame)
        self.output_display.pack(ipady=5)
        self.output_display.config(bg="#ff2052",fg="white")
        return self.game_frame
        

if __name__ == "__main__":
    game= number_guessing_game()
    game.mainloop()
