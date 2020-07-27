from tkinter import *

def infos():
    print(first_name_value.get())
    print(last_name_value.get())
    print(address_value.get())
    print(phone_number_value.get())
    print(age_value.get())
    print(gender_value.get())
    print(email_value.get())



root= Tk()
root.geometry("333x555")

first_name =Label(root, text="First Name : ")
last_name =Label(root, text="Last Name : " )
address =Label(root, text="Address : ")
phone_number =Label(root, text="Phone Number : ")  
age =Label(root, text="Age : ")
gender =Label(root, text="Gender : ")
email =Label(root, text="Email : ")
first_name.grid(pady=16)
last_name.grid(pady=16)
address.grid(pady=16)
phone_number.grid(pady=16)
age.grid(pady=16)
gender.grid(pady=16)
email.grid(pady=16)

first_name_value= StringVar()
last_name_value= StringVar()
address_value= StringVar()
phone_number_value= StringVar()
age_value= StringVar()
gender_value= StringVar()
email_value= StringVar()

first_name_Entry= Entry(root, textvariable= first_name_value)
last_name_Entry= Entry(root, textvariable= last_name_value)
address_Entry= Entry(root, textvariable= address_value)
phone_number_Entry= Entry(root, textvariable= phone_number_value)
age_Entry= Entry(root, textvariable= age_value)
gender_Entry= Entry(root,textvariable=gender_value)
email_Entry= Entry(root, textvariable= email_value)

first_name_Entry.grid(row=0,column=1, pady=16)
last_name_Entry.grid(row=1,column=1, pady=16)
address_Entry.grid(row=2,column=1, pady=16)
phone_number_Entry.grid(row=3,column=1, pady=16)
age_Entry.grid(row=4,column=1, pady=16)
gender_Entry.grid(row=5,column=1, pady=16)
email_Entry.grid(row=6,column=1, pady=16)

Submit_Button = Button(root,text="Submit" , bg="orange" , fg="green", command=infos).grid()
root.mainloop()
