from tkinter import *
from PIL import Image,ImageTk
from time import sleep
import tkinter.messagebox as tmsg
import random
class stone_paper_scissor(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x800+300+2")
        self.title("Stone Paper Scissors")
        self.frame= None
        self.swap_frame(self.opening_frame_func())
    def result(self,computer_choice,user_choice):
        if (computer_choice=="rock" and user_choice=="scissors") or (computer_choice=="paper" and user_choice=="rock") or (computer_choice=="scissors" and user_choice=="paper"):
            self.comp_score+=1
            return "lose","win"
        elif (user_choice=="rock" and computer_choice=="scissors") or (user_choice=="paper" and computer_choice=="rock") or (user_choice=="scissors" and computer_choice=="paper"):
            self.user_score+=1
            return "win","lose"
        else:
            return "win","win"
    def final_result(self):
        if self.comp_score<self.user_score:
            return "win","You win"
        elif self.comp_score>self.user_score:
            return "lose","You Lose"
        else:
            return "tie","Its a tie breaker"
    def reset(self):
        result,statement=self.final_result()
        value= tmsg.askquestion(result,f"{statement},Wanna play it again!!")
        if value=="yes":
            self.swap_frame(self.game_frame_func())
        if value=="no":
            self.swap_frame(self.opening_frame_func())
    def display(self,event):  
        if self.round_count<self.rounds:
            self.round_count+=1
            self.round_label.config(text="Rounds "+str(self.round_count))
            self.user_select= event.widget.cget("text").lower()
            self.choices=["rock","paper","scissors"]
            self.comp_select= random.choice(self.choices)
            user_result,comp_result=self.result(self.comp_select,self.user_select)
            if self.user_select=="scissors":
                self.temp_user= self.open_image(f"stone_paper_scissors/images/{self.user_select}_user_{user_result}.png",150,150)
            else:
                self.temp_user= self.open_image(f"stone_paper_scissors/images/{self.user_select}_{user_result}.png",150,150)
            self.user_choice.config(image=self.temp_user)
            self.user_choice_temp=self.open_image(f"stone_paper_scissors/images/{self.comp_select}_{comp_result}.png",150,150)
            self.computer_choice.config(image=self.user_choice_temp)
            self.score_label.config(text=f"{self.user_score}  ⓋⓈ  {self.comp_score}")
            if user_result=="win" and comp_result=="win":
                self.temp_result=self.open_image(f"stone_paper_scissors/images/tie.png",200,200)
            else:
                self.temp_result=self.open_image(f"stone_paper_scissors/images/{user_result}.png",200,200)          
            self.result_label.config(image=self.temp_result)
            self.user_name_label.grid_forget()
            self.comp_name_label.grid_forget()
            self.user_name_label.grid(column=1,row=5,ipady=10,ipadx=40,padx=20)
            self.comp_name_label.grid(column=3,row=5,ipady=10,ipadx=40)
            if self.rounds==self.round_count:
                self.reset()
            
        
    def check_entry(self):
        if self.name_entry.get()=="":
            self.error.config(text="*Please enter a name")
        else:
            self.user_name= self.name_entry.get()
            print(self.user_name)
            self.rounds=self.rounds_slider.get()
            print(type(self.rounds))
            self.swap_frame(self.game_frame_func())


    def swap_frame(self,new_frame):
        if self.frame is not None:
            self.frame.destroy()
        self.frame= new_frame
        self.frame.pack(expand=True,fill=BOTH)

    def correct(self,inp):
        if len(inp)>25:
            return False
        else:
            return True
    def open_image(self,address,height,width):
        self.image_open= Image.open(address)
        self.image_resize= self.image_open.resize((height,width),Image.ANTIALIAS)
        self.image_resized= ImageTk.PhotoImage(self.image_resize)
        return self.image_resized
    def opening_frame_func(self):
        self.opening_frame= Frame(self,bg="#0392cf")
        self.opening_frame_image= Label(self.opening_frame,bd=10,bg="#f37736",image=self.open_image("stone_paper_scissors/images/r_p_s.png",700,400))
        self.opening_frame_image.pack(pady=50)
        self.start_button= Button(self.opening_frame,text="Start Game",font="verdana 30 bold",bg="#3da4ab",fg="#fdf5e6",cursor="hand2",command=lambda : self.swap_frame(self.rounds_and_name_func()))
        self.start_button.pack(pady=40)
        return self.opening_frame
        
    def rounds_and_name_func(self):
        self.rounds_and_name= Frame(self,bg="#FFD3B5")
        self.main_heading= Label(self.rounds_and_name,image=self.open_image("stone_paper_scissors/images/head_image.png",600,100))
        self.main_heading.pack(pady=50)
        self.name= Label(self.rounds_and_name,text="Player Name",font="sansserif 20 bold underline",bg="#FFD3B5",fg="#251e3e")
        self.name.pack(pady=10,fill=X,padx=60)
        self.name_entry= Entry(self.rounds_and_name,font="helvatica 20 bold",justify=CENTER)
        self.name_reg= self.rounds_and_name.register(self.correct)
        self.name_entry.config(validate="key",validatecommand=(self.name_reg,'%P'))
        self.name_entry.focus()
        self.name_entry.pack(pady=(10,10),ipady=10)
        self.rounds= Label(self.rounds_and_name,text="Rounds",font="sansserif 20 bold underline",bg="#FFD3B5",fg="#251e3e")
        self.rounds.pack(fill=X,padx=60,pady=(50,10))
        self.rounds_slider= Scale(self.rounds_and_name,from_=1, to_=31,orient=HORIZONTAL,tickinterval=2,font="arialblack 10 bold",relief=GROOVE,bg="#851e3e",fg="white",troughcolor="#FFD3B5",takefocus=10,cursor="hand2")
        self.rounds_slider.set(3)
        self.rounds_slider.pack(pady=30,fill=X,padx=30,ipady=10,ipadx=90)
        self.submit= Button(self.rounds_and_name,text="Play ▶",font="sansserif 20 bold",bg="#251e3e",fg="#ffffff",cursor="hand2",command=self.check_entry)
        self.submit.pack(pady=30,ipady=10,ipadx=70)
        self.error= Label(self.rounds_and_name,font="sensserif 20 bold",bg="#FFD3B5",fg="red")
        self.error.pack(pady=10)
        return self.rounds_and_name

    def game_frame_func(self):
        self.comp_score=0
        self.user_score=0
        self.round_count=0
        self.game_frame= Frame(self,bg="#F8E1B4")
        self.heading_temp= self.open_image("stone_paper_scissors/images/head_image.png",600,100)
        self.heading= Label(self.game_frame,image=self.heading_temp)
        self.heading.grid(column=1,row=1,columnspan=5,padx=50)
        self.rock_button= Button(self.game_frame,text="Rock",font="verdana 20 bold",bg="#F7FF3F",cursor="hand2")
        self.rock_button.bind("<Button-1>",self.display)
        self.rock_button.grid(column=1,row=2,pady=10,padx=40)
        self.paper_button= Button(self.game_frame,text="Paper",font="verdana 20 bold",bg="#F7FF3F",cursor="hand2")
        self.paper_button.bind("<Button-1>",self.display)
        self.paper_button.grid(column=2,row=2,pady=10)
        self.scissors_button= Button(self.game_frame,text="Scissors",font="verdana 20 bold",bg="#F7FF3F",cursor="hand2")
        self.scissors_button.bind("<Button-1>",self.display)
        self.scissors_button.grid(column=3,row=2,pady=10)
        self.round_label= Label(self.game_frame,text="Round 1",bg="#F8E1B4",font="system 30 bold")
        self.round_label.grid(column=2,row=3,pady=10)
        self.user_choice= Label(self.game_frame,bg="#F8E1B4")
        self.user_choice.grid(column=1,row=4,ipadx=20)
        self.computer_choice= Label(self.game_frame,bg="#F8E1B4",)
        self.computer_choice.grid(column=3,row=4)
        self.user_name_label= Label(self.game_frame,text=self.user_name.upper(),font="sensserif 20 bold underline",fg="#FF2321",bg="#cbe54e",bd=10)
        self.user_name_label.grid(column=1,row=4,ipady=10,ipadx=40,padx=20)
        self.comp_name_label= Label(self.game_frame,text="Computer",font="sensserif 20 bold underline",fg="#FF2321",bg="#cbe54e",bd=10)
        self.comp_name_label.grid(column=3,row=4,ipady=10,ipadx=40)
        self.score_label= Label(self.game_frame,bg="#F8E1B4",text=f"{self.user_score}                     {self.comp_score}",font="algerian 30")
        self.score_label.grid(column=2,row=4)
        self.vs_pic_temp= self.open_image("stone_paper_scissors/images/vs.png",100,200)
        self.vs= Label(self.game_frame,image=self.vs_pic_temp,bg="#F8E1B4")
        self.vs.grid(column=2,row=4,pady=20)
        self.result_label= Label(self.game_frame,bg="#F8E1B4")
        self.result_label.grid(column=2,row=5)
        for i in range(1,5):
            if i<=3:
                Grid.columnconfigure(self.game_frame,i,weight=9)
            Grid.rowconfigure(self.game_frame,i,weight=9)
        return self.game_frame



if __name__ == "__main__":
    play= stone_paper_scissor()
    play.mainloop() 