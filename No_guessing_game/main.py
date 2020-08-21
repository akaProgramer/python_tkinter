from tkinter import *


class number_guessing_game(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.open_frame_content()

    def open_frame_content(self):
        self.open_frame= Frame(self)
        self.open_frame.config(bg="#ffd700")
        self.start_photo= Label(self.open_frame,text="Welcome to the game")
        self.start_photo.pack()
        self.start_button= Button(self.open_frame,text= "Start the Game")
        self.start_button.pack()
        self.open_frame.pack()
        

if __name__ == "__main__":
    game= number_guessing_game()
    game.mainloop()
