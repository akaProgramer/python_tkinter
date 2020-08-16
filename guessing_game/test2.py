# import tkinter as tk # Python 3
# root = tk.Tk()
# # The image must be stored to Tk or it will be garbage collected.
# root.image = tk.PhotoImage(file='guessing_game/guess.png')
# label = tk.Label(root, image=root.image, bg='white')
# root.overrideredirect(True)
# root.geometry("+250+250")
# root.lift()
# root.wm_attributes("-topmost", True)
# # root.wm_attributes("-disabled", True)
# root.wm_attributes("-transparentcolor", "white")
# label.pack()
# label.mainloop()
import tkinter as tk

maxbutton = 5
maxkey = str(maxbutton)

def button_cb(ch):
    print('Button ' + ch + ' pressed')

def onKeyPress(event):
    ch = event.char
    if '1' <= ch <= maxkey:
        #Retrieve this button from the dict
        b = buttons[ch]

        #Simulate pushing the button
        b.config(relief=tk.SUNKEN)
        button_cb(ch)

        #Let it pop back up after 200 milliseconds
        b.after(200, lambda: b.config(relief=tk.RAISED))

root = tk.Tk()
root.title("Key / Button Demo")

#A dict to save the buttons in. The dict keys are the button texts.
buttons = {}

#Make some buttons
for i in range(1, maxbutton + 1):
    s = str(i)
    b = tk.Button(root, text=s, command=lambda ch=s: button_cb(ch))
    b.pack(side=tk.LEFT)

    #Save this button in the dict
    buttons[s] = b

root.bind('<KeyPress>', onKeyPress)

root.mainloop()