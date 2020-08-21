from tkinter import *
root= Tk()
root.geometry("111x111")
f1= Frame(root)

f2= Frame(root)
for frame in (f1,f2):
    frame.grid(column=0, row= 0,sticky=N+S+E+W)

def is_visible(widget):
    try:
        widget.winfo_visualsavailable()
    except TclError:
        # pack_info raises if pack hasn't been
        # called yet.
        return bool(widget.grid_info())
        # grid_info returns {} if grid hasn't been
        # called yet.
    else:
        return True


print(is_visible(f2))
def switch_frame(frame):
    frame.tkraise()


Label(f1, text="Start page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
Button(f1, text="Go to page one",
                  command=lambda: switch_frame(f2)).pack()
Label(f2, text="Page one", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
Button(f2, text="Go back to start page",
                  command=lambda: switch_frame(f1)).pack()
switch_frame(f1)
is_visible(f1)

root.mainloop()



