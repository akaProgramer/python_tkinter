from tkinter import *
from PIL import Image,ImageTk
import random
import re
import tkinter.messagebox as tmsg
from time import sleep
total = {
    "Flower": [
        "rose",
        "jasmine",
        "lilly",
        "tulip",
        "snowdrops",
        "lotus",
        "cherry",
        "sunflower",
        "daisy"
    ],
    "Animal": ["dog", "cat", "elephant", "horse", "lion", "tiger", "cheetah", "bear", "dear","crocodile","pig","cow","buffalo","goat"
    ,"hippopotamus"],
    "Computer Part or\n Accessories": [
        "mouse",
        "keyboard",
        "monitor",
        "speaker",
        "processor",
        "motherboard",
        "pendrive",
        "UPS",
        "microphone",
        "webcam",
        "headphone"
    ],
    "Body Part": [
        "fingers",
        "toe",
        "leg",
        "hairs",
        "eyes",
        "nose",
        "ears",
        "lips",
        "hips",
        "mouth",
        "knee",
        "toe",
        "elbow",
        "thumb"
    ],
    "Game": ["football","basketball","cricket","volleyball","badminton","table tennis","lawn tennis"],
    "Vegetable": ["onion","potato","cabbage","tomato","cucumber","raddish","carrot","sweet potato","cauliflower","spinach","brinjal",
    "lady finger"]
}

random_list = ""
random_word = ""
guess_word= ""


root= Tk()
root.title("Guess the word")
root.minsize(810,600)
root.geometry("890x700+300+60")
# root.config(background="black")


def pressButton(b): 
    b.config(relief="sunken",fg="#f0e6f9", bg="#f0162b")
    b.after(100, lambda button=b: button.config(relief="raised",bg="#f0162b",fg="yellow"))
    try:
        check_ans()
    except:
        print("noop")

def correct(inp):
    if len(inp)>25:
        output_display.config(text="*Character limit exceed",fg="#d62d20",bg="#ffffff")
        return False
    elif inp.isalpha() or " " in inp:
        output_display.config(text="",bg="orange")
        return True
    elif inp is "":
        return True
    else:
        output_display.config(text="*Aphabets are allowed only!!",fg="#d62d20",bg="#ffffff")
        return False


temp=[]
def update_display():
    global guess_word,temp
    random_number= random.randint(0,len(guess_word)-1)
    if random_number not in temp:
        guess_word= guess_word[:random_number] + random_word[random_number] + guess_word[random_number+1:]
        temp.append(random_number)
    else:
        update_display()
    spacing= " ".join(guess_word)
    return spacing


attempt= 0

def no_of_attempts():
    word_len= len(random_word)
    if word_len<=5:
        return (word_len//2)+1
    elif word_len>5 and word_len<=7:
        return (word_len//2)
    elif word_len>7 and word_len<=10:
        return (word_len//2)+1
    else:
        return 6

def reset(result):
    global temp
    value= tmsg.askquestion(result,"Wanna! play it again")
    if value=="yes":
        value_set()  
        answer.delete(0,END)
        display_var.set(f"{update_display()}")
        hint_label.config(text="")
        output_display.config(text="")
        output_display.config(bg="orange")
        hint_label.config(text=f"Hint:- Its a name of {random_list}")
    else:
        switch_frame(opening_frame_build())
    temp=[]

def value_set():
    global random_list,random_word,attempt,guess_word
    random_list = random.choice(list(total.keys()))
    random_word = random.choice(total[random_list])
    guess_word= re.sub('[a-zA-Z]','_',random_word)
    attempt=no_of_attempts()

def check_ans():
    global attempt
    attempt-=1
    answervar= user_answer.get().lower().replace(" ","")
    if answervar=="":
            output_display.config(text="Dont leave it empty",fg="#d62d20",bg="#ffffff")
            attempt+=1
            return
    elif attempt>=0:
        if answervar!=random_word.lower().replace(" ","") and attempt>0:
            if len(answervar)>1 and answervar in random_word.lower().replace(" ",""):
               hint_label.config(text=f"It Was close")
            else:
                display_var.set(update_display())
            output_display.config(text="Incorrect !!",fg="#d62d20",bg="#ffffff")
            answer.delete(0,END)
        elif answervar==random_word.lower().replace(" ",""):
            print("correct")
            display_var.set(" ".join(random_word))
            output_display.config(text=f"Well Done!! you guessed it in {no_of_attempts()-attempt} attempts",fg="green",bg="#ffffff")
            attempt_label.config(text=f"Attempts {attempt}")
            reset("Win!!")
        else:
            output_display.config(text=f'''You loose, no more attempts left the word was "{random_word}"''',fg="#d62d20",bg="#ffffff")
            attempt_label.config(text=f"Attempts {attempt}")
            display_var.set(" ".join(random_word))
            reset("Loose!!")
        attempt_label.config(text=f"Attempts {attempt}")


frame= None
def switch_frame(new_frame):
    global frame
    if frame is not None:
        frame.destroy()
        print(frame)
    frame = new_frame
    frame.grid(column=0, row= 0,sticky=N+S+E+W)
    Grid.rowconfigure(root,0,weight=1)
    Grid.columnconfigure(root,0,weight=1)

def opening_frame_build():
    global var_photo
    opening_frame= Frame(root,highlightthickness=10)
    opening_frame.config(highlightbackground="#f0f3f5",highlightcolor="#f0f3f5",bg="#deefb7")
    photo= Image.open("guessing_game/guess.png")
    resize= photo.resize((600,300),Image.ANTIALIAS)
    resized_image= ImageTk.PhotoImage(resize)
    var_photo=Label(opening_frame,image=resized_image,relief=SUNKEN,highlightcolor="black",highlightbackground="black",highlightthickness=20)
    var_photo.image= resized_image
    var_photo.pack(pady=30)
    start_button=Button(opening_frame, text="START GAME", bg="#ffd700",fg="black", activebackground="#ffd700",activeforeground="#f0e6f9" ,font="sensserif 30 bold",borderwidth=1,relief=RAISED,cursor="hand2", command=lambda :switch_frame(game_frame_build()))
    start_button.pack(pady=30)
    start_button.bind("<Button-1>",value_set())
    return opening_frame


def game_frame_build():
    global display_var,user_answer,output_display,attempt_label,hint_label,answer
    game_frame= Frame(root,highlightthickness=10,bg="orange")
    game_frame.config(highlightbackground="#f0f3f5",highlightcolor="#f0f3f5",relief=SUNKEN,borderwidth=6)
    heading=Label(game_frame,text="Guess The Word If You Can",font="bodonimt 40 bold underline",bg="#67C8FF",fg="#ffffff")
    heading.pack(pady=30,fill=X)

    display_var=StringVar()
    display_var.set(f"{update_display()}")

    display= Label(game_frame, textvariable=display_var,relief=RIDGE,bd=3,width=34, font="mullish 25",bg="#0066cc",fg="white",height=2,justify=CENTER)
    display.pack(pady=40)


    user_answer= StringVar()
    answer= Entry(game_frame,font="arialblack 24", borderwidth=6,textvariable=user_answer,relief=SUNKEN,bg="#cfefff",justify=CENTER)
    answer.pack(padx=40,pady=40,ipady=7)
    reg= game_frame.register(correct)
    answer.config(validate="key",validatecommand=(reg,'%P'))

    Checkbutton= Button(game_frame, text= "CHECK", font="roboto 20 bold",borderwidth=6,bg="#f0162b",fg="yellow", activebackground="#f0162b",activeforeground="#f0e6f9",cursor="hand2",command= check_ans)
    root.bind("<Return>",lambda e, b=Checkbutton: pressButton(b))
    Checkbutton.pack()

    output_display= Label(game_frame,font="calibri 19 bold",justify=CENTER,bg="orange")
    output_display.pack(pady=30,ipadx=10)

    attempt_label= Label(game_frame,text=f"Attempts {attempt}",font="roboto 20 bold",bg="#ff6f69",padx=10,pady=10,fg="#ffffff")
    attempt_label.pack(side=RIGHT,padx=20)

    hint_label= Label(game_frame,font="arialblack 24",text=f"Hint:- Its a name of {random_list}",bg="#fdf498",padx=10,pady=10,fg="#0392cf")
    hint_label.pack(side=LEFT,padx=14)
    return game_frame


switch_frame(opening_frame_build())

root.mainloop()

