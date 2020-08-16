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
    "Animal": ["dog", "cat", "elephant", "horse", "lion", "tiger", "cheetah", "bear", "dear"],
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
    "Game": ["football","basketball","cricket","volleyball","badminton","table tennis","lawn tennis"]
}

random_list = ""
random_word = ""
guess_word= ""


root= Tk()
root.title("Guess the word")
root.minsize(810,600)
root.geometry("890x700")
# root.config(background="black")
opening_frame= Frame(root,highlightthickness=10)
opening_frame.config(highlightbackground="#f0f3f5",highlightcolor="#f0f3f5")
game_frame= Frame(root,highlightthickness=10)
game_frame.config(highlightbackground="#f0f3f5",highlightcolor="#f0f3f5",relief=SUNKEN,borderwidth=6)

root.attributes("-transparent","red")
def pressButton(b): 
    b.config(relief="sunken",fg="#f0e6f9", bg="#ffd700")
    game_frame.after(100, lambda button=b: button.config(relief="raised",bg="#f0162b",fg="yellow"))
    check_ans()

def correct(inp):
    if len(inp)>25:
        output_display.config(text="*Character limit exceed",fg="#d62d20")
        return False
    elif inp.isalpha() or " " in inp:
        output_display.config(text="")
        return True
    elif inp is "":
        return True
    else:
        output_display.config(text="*Aphabets are allowed only!!",fg="#d62d20")
        return False

def no_of_attempts():
    word_len= len(random_word)
    if word_len<=5:
        return (word_len//2)+1
    elif word_len>5 and word_len<=10:
        return (word_len//2)-1
    else:
        return 6

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

def swap(frame):
    frame.tkraise()


attempt= 0
def value_set():
    global random_list,random_word,attempt,guess_word
    random_list = random.choice(list(total.keys()))
    random_word = random.choice(total[random_list])
    guess_word= re.sub('[a-zA-Z]','_',random_word)
    attempt=no_of_attempts()


def reset(result):
    global temp
    value= tmsg.askquestion(result,"Wanna! play it again")
    if value=="yes":
        value_set()
    else:
        value_set()
        swap(opening_frame)
    answer.delete(0,END)
    display_var.set(f"{update_display()}")
    hint_label.config(text="")
    output_display.config(text="")
    hint_label.config(text=f"Hint:- Its a name of {random_list}")
    temp=[]

def check_ans():
    global attempt
    attempt-=1
    answervar=user_answer.get().lower().replace(" ","")
    if answervar=="":
            output_display.config(text="Dont leave it empty",fg="#d62d20")
            attempt+=1
            return
    elif attempt>=0:
        if answervar!=random_word.lower().replace(" ","") and attempt>0:
            if len(answervar)>1 and answervar in random_word.lower().replace(" ",""):
                hint_label.config(text=f"It Was too close")
            else:
                display_var.set(update_display())
            output_display.config(text="Incorrect !!",fg="#d62d20")
            answer.delete(0,END)
        elif answervar==random_word.lower().replace(" ",""):
            print("correct")
            display_var.set(" ".join(random_word))
            output_display.config(text=f"Well Done!! you guessed it in {no_of_attempts()-attempt} attempts",fg="green")
            attempt_label.config(text=f"Attempts {attempt}")
            reset("Win!!")
        else:
            output_display.config(text=f'''You loose, no more attempts left the word was "{random_word}"''',fg="#d62d20")
            attempt_label.config(text=f"Attempts {attempt}")
            display_var.set(" ".join(random_word))
            reset("Loose!!")
        attempt_label.config(text=f"Attempts {attempt}")
Grid.rowconfigure(root,0,weight=1)
Grid.columnconfigure(root,0,weight=1)

opening_frame.config(bg="#deefb7")
game_frame.config(bg="orange")
for frame in (opening_frame,game_frame):
    frame.grid(column=0, row= 0,sticky=N+S+E+W)

photo= Image.open("guessing_game/guess.png")
resize= photo.resize((600,300),Image.ANTIALIAS)
resized_image= ImageTk.PhotoImage(resize)
Label(opening_frame,image=resized_image,relief=SUNKEN,highlightthickness=20,highlightcolor="black",highlightbackground="black").pack(pady=30)

# Label(opening_frame,text="Word Guessing Game",font="helvetica 50 bold underline").pack(pady=100)
start_button=Button(opening_frame, text="START GAME", bg="#ffd700",fg="black", activebackground="#ffd700",activeforeground="#f0e6f9" ,font="sensserif 30 bold",borderwidth=1,relief=RAISED,cursor="hand2", command=lambda :swap(game_frame))
start_button.pack(pady=30)
start_button.bind("<Button-1>",value_set())

heading=Label(game_frame,text="WELCOME TO THE GAME",font="bodonimt 40 bold underline",bg="#67C8FF",fg="#ffffff")
heading.pack(pady=30,fill=X)

display_var=StringVar()
display_var.set(f"{update_display()}")

display= Label(game_frame, textvariable=display_var,relief=RIDGE,bd=3,width=34, font="mullish 25",bg="#0066cc",fg="white",height=2,justify=CENTER)
display.pack(pady=40)


user_answer= StringVar()

answer= Entry(game_frame,font="arialblack 24", borderwidth=6,textvariable=user_answer,relief=SUNKEN,bg="#cfefff",justify=CENTER)
answer.pack(padx=40,pady=40,ipady=7)
answer.focus()
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

swap(opening_frame)
root.mainloop()

