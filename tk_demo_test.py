#Creating Database and Table
import sqlite3 as db

database=db.connect('Dance.db')#Creating the database
table=database.cursor()
table.execute('''CREATE TABLE IF NOT EXISTS DATA 
(First_Name TEXT,
Last_Name TEXT,
Email TEXT,
Country TEXT,
State TEXT,
City TEXT)''')#Creating table with headings
table.close()
database.commit()
database.close()

#Adding the data into the database
def put():
    database=db.connect('Dance.db')
    table=database.cursor()
    table.execute('''insert into DATA values
    ('%s','%s','%s','%s','%s','%s')'''%(fname.get(),lname.get(),evar.get(),cvar.get(),svar.get(),cityvar.get()))#Inserting data into the table
    table.close()
    database.commit()
    database.close()
    covar.set('Data Added Successfully')#Printing the message as soon as the data is added into the table

#Creating the code for the working of the 'Next' button    
def move_on():
    global confirm #Globalising the label variable so that it can be viewed everywhere
    #Deleting the contents in the entry boxes as soon as the 'Next' button is pressed
    f_entry.delete(0,END)
    l_entry.delete(0,END)
    email_entry.delete(0,END)
    c_entry.delete(0,END)
    s_entry.delete(0,END)
    city_entry.delete(0,END)
    #Deleting the confirmation message as soon as the 'Next' button is pressed so that a fresh message is displayed later on
    confirm.destroy()
    covar.set('')
    confirm=Label(root,text='',textvariable=covar,padx=5,pady=5,bg="cyan",fg="green")
    confirm.grid(row=5,columnspan=4)

#Creating the code for the working of the 'Quit' button
def Quit():
    root.destroy()

#Creating the GUI
from tkinter import *
                  
root=Tk() #Creating the instance
root.geometry("675x430")
root.configure(bg="cyan",borderwidth=5,relief=RIDGE,highlightthickness=5,highlightcolor="maroon")#Decorating the instance
root.title("Dance Form")

#Creating the variables
fname=StringVar()
lname=StringVar()
evar=StringVar()
cvar=StringVar()
svar=StringVar()
cityvar=StringVar()
covar=StringVar()

head=Label(root,text="Dancing Guru",padx=5,pady=5,bg="light blue",font="comicsansms 26 bold",
           borderwidth=5,relief=RIDGE)#Title label
head.grid(row=0,columnspan=4,padx=10,pady=10)

f=Label(root,text="First Name",padx=5,pady=5,bg="yellow",borderwidth=5,relief=SUNKEN,font="comicsansms 13 italic")#First name label
f.grid(row=1,column=0,padx=10,pady=10)
f_entry=Entry(root,textvariable=fname,borderwidth=5,relief=GROOVE,font="comicsansms 13 italic")#First name entry
f_entry.grid(row=1,column=1,padx=10,pady=10)

l=Label(root,text="Last Name",padx=5,pady=5,borderwidth=5,relief=SUNKEN,bg="yellow",font="comicsansms 13 italic")#Last name label
l.grid(row=2,column=0,padx=10,pady=10)
l_entry=Entry(root,textvariable=lname,borderwidth=5,relief=GROOVE,font="comicsansms 13 italic")#Last name entry
l_entry.grid(row=2,column=1,padx=10,pady=10)

email=Label(root,text="E-mail",padx=5,pady=5,borderwidth=5,relief=SUNKEN,bg="yellow",font="comicsansms 13 italic")#Email label
email.grid(row=3,column=0)
email_entry=Entry(root,textvariable=evar,borderwidth=5,relief=GROOVE,font="comicsansms 13 italic")#Email entry
email_entry.grid(row=3,column=1,padx=10,pady=10)

country=Label(root,text="Country",padx=5,pady=5,borderwidth=5,relief=SUNKEN,bg="yellow",font="comicsansms 13 italic")#Country label
country.grid(row=1,column=2,padx=10,pady=10)
c_entry=Entry(root,textvariable=cvar,borderwidth=5,relief=GROOVE,font="comicsansms 13 italic")#Country entry
c_entry.grid(row=1,column=3,padx=10,pady=10)

state=Label(root,text="State",padx=5,pady=5,borderwidth=5,relief=SUNKEN,bg="yellow",font="comicsansms 13 italic")#State label
state.grid(row=2,column=2,padx=10,pady=10)
s_entry=Entry(root,textvariable=svar,borderwidth=5,relief=GROOVE,font="comicsansms 13 italic")#State entry
s_entry.grid(row=2,column=3,padx=10,pady=10)

city=Label(root,text="City",padx=5,pady=5,borderwidth=5,relief=SUNKEN,bg="yellow",font="comicsansms 13 italic")#City label
city.grid(row=3,column=2,padx=10,pady=10)
city_entry=Entry(root,textvariable=cityvar,borderwidth=5,relief=GROOVE,font="comicsansms 13 italic")#City entry
city_entry.grid(row=3,column=3,padx=10,pady=10)

submit=Button(root,text="Submit",padx=5,pady=5,command=put,bg="orange",font="comicsansms 13 italic",borderwidth=5,relief=RAISED)#Submit button
submit.grid(row=4,column=0,columnspan=2,padx=10,pady=10)

Next=Button(root,text="Next",padx=5,pady=5,command=move_on,bg="orange",font="comicsansms 13 italic",borderwidth=5,relief=RAISED)#Next button
Next.grid(row=4,column=2,columnspan=1,padx=10,pady=10)

q=Button(root,text="Quit",padx=5,pady=5,command=Quit,bg="orange",font="comicsansms 13 italic",borderwidth=5,relief=RAISED)#Quit button
q.grid(row=4,column=3,columnspan=3,padx=10,pady=10)

confirm=Label(root,text='',textvariable=covar,padx=5,pady=5,bg="cyan",fg="green",font="comicsansms 20 italic")#Confirmation ('Data Added Successfully') label
confirm.grid(row=5,columnspan=4,padx=10,pady=10)

root.mainloop()