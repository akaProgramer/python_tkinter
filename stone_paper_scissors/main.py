from tkinter import *
from PIL import Image,ImageTk
from time import sleep
import random
class stone_paper_scissor(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("900x800+300+10")
        self.title("Stone Paper Scissors")
        # self.rounds_and_name_func()
        self.game_frame_func()
        # self.frame= None
        # self.swap_frame(self.opening_frame_func())
    def result(self,computer_choice,user_choice):
        if (computer_choice=="rock" and user_choice=="scissors") or (computer_choice=="paper" and user_choice=="rock") or (computer_choice=="scissors" and user_choice=="paper"):
            self.comp_score+=1
            return "lose","win"
        elif (user_choice=="rock" and computer_choice=="scissors") or (user_choice=="paper" and computer_choice=="rock") or (user_choice=="scissors" and computer_choice=="paper"):
            self.user_score+=1
            return "win","lose"
        else:
            return "win","win"
    def display(self,event):
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
    def check_entry(self):
        if self.name_entry.get()=="":
            self.error.config(text="*Please enter a name")
        else:
            self.user_name= self.name_entry.get()
            print(self.user_name)
            self.rounds=self.rounds_slider.get()
            print(self.rounds)
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
        self.name= Label(self.rounds_and_name,text="Player Name",font="sansserif 20 bold",bg="#FFD3B5",fg="#251e3e")
        self.name.pack(pady=10,fill=X,padx=60)
        self.name_entry= Entry(self.rounds_and_name,font="helvatica 20 bold",justify=CENTER)
        self.name_reg= self.rounds_and_name.register(self.correct)
        self.name_entry.config(validate="key",validatecommand=(self.name_reg,'%P'))
        self.name_entry.pack(pady=10,ipady=10)
        self.rounds= Label(self.rounds_and_name,text="Rounds",font="sansserif 20 bold",bg="#FFD3B5",fg="#251e3e")
        self.rounds.pack(fill=X,padx=60)
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
        self.game_frame= Frame(self,bg="skyblue")
        self.heading_temp= self.open_image("stone_paper_scissors/images/head_image.png",600,100)
        self.heading= Label(self.game_frame,image=self.heading_temp)
        self.heading.grid(column=4,row=1,pady=10)
        self.rock_button= Button(self.game_frame,text="Rock")
        self.rock_button.bind("<Button-1>",self.display)
        self.rock_button.grid(column=3,row=2,padx=70,pady=40)
        self.paper_button= Button(self.game_frame,text="Paper")
        self.paper_button.bind("<Button-1>",self.display)
        self.paper_button.grid(column=4,row=2,padx=70,pady=40)
        self.scissors_button= Button(self.game_frame,text="Scissors")
        self.scissors_button.bind("<Button-1>",self.display)
        self.scissors_button.grid(column=5,row=2,padx=70,pady=40)
        self.score_label_temp= self.open_image("stone_paper_scissors/images/score.png",100,50)
        self.score_pic= Label(self.game_frame,image=self.score_label_temp,bg="skyblue")
        self.score_pic.grid(column=4,row=3,pady=10)
        self.user_choice= Label(self.game_frame,bg="skyblue")
        self.user_choice.grid(column=3,row=4,padx=20)
        self.computer_choice= Label(self.game_frame,bg="skyblue")
        self.computer_choice.grid(column=5,row=4)
        self.score_label= Label(self.game_frame,text=f"{self.user_score}           ⓋⓈ                  {self.comp_score}",font="algerian 30")
        self.score_label.grid(column=4,row=5)
        self.result_label= Label(self.game_frame)
        self.result_label.grid(column=4,row=6,pady=50)
        for j in range(1,7):
            Grid.rowconfigure(self.game_frame,j,weight=1)
        Grid.columnconfigure(self.game_frame,5,weight=1)
        Grid.columnconfigure(self.game_frame,4,weight=1)
        Grid.columnconfigure(self.game_frame,3,weight=1)
        self.game_frame.pack(fill=BOTH,expand=True)


if __name__ == "__main__":
    play= stone_paper_scissor()
    play.mainloop() 