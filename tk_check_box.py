from tkinter import *


def print_values():
    print(mobile_brand_value.get())
    print(processor_value.get())
    print(ram_value.get())
    print(storage_value.get())
    print(os_value1.get())
    with open("phone.txt","a") as f:
        f.write(f"{mobile_brand_value.get(),processor_value.get(),ram_value.get(),storage_value.get(),os_value1.get()}\n")

root= Tk()
root.minsize(700,500)
root.title("Mobile Information")

# root.configure(bg="yellow")

Label(root, text="Moblie Specs", font="arialblack 24 bold underline", fg="green", bg="yellow").grid(column=2, row=1,pady=15)
mobile_brand= Label(root,text="Mobile Brand Name: ", font="comicsansms 12 bold", fg="orange")
processor= Label(root, text="Processor: ", font="comicsansms 12 bold", fg="orange")
ram= Label(text="Size of RAM: ", font="comicsansms 12 bold", fg="orange")
storage= Label(text="Storage (in Gb): ", font="comicsansms 12 bold", fg="orange")
os= Label(text="OS: ", font="comicsansms 12 bold", fg="orange")

mobile_brand.grid(row=6 , column= 1,padx= 9)
processor.grid(row= 7, column= 1,padx= 9)
ram.grid(row= 8, column= 1,padx= 9)
storage.grid(row= 9, column= 1,padx= 9)
os.grid(row=10, column= 1,padx= 9)

mobile_brand_value= StringVar()
processor_value= StringVar()
ram_value= StringVar()
storage_value= StringVar()
os_value1= StringVar()
os_value1.set("NULL")

mobile_brand_entry= Entry(root, textvariable=mobile_brand_value)
processor_entry= Entry(root, textvariable=processor_value)
ram_entry= Entry(root, textvariable=ram_value)
storage_entry= Entry(root, textvariable=storage_value)
os_entry1= Radiobutton(root, text="Android", variable=os_value1, value="Android")
os_entry2= Radiobutton(root, text="IOS", variable=os_value1, value= "IOS")

mobile_brand_entry.grid(row= 6, column= 2,padx= 9)
processor_entry.grid(row= 7, column= 2,padx= 9)
ram_entry.grid(row= 8, column= 2,padx= 9)
storage_entry.grid(row= 9, column= 2,padx= 9)
os_entry1.grid(row= 10, column= 2, padx=9)
os_entry2.grid(row= 10, column= 3, padx=9)

submit_button= Button(text="Submit", bg="grey",relief=RAISED, command=print_values)
submit_button.grid(row=14, column=2, pady= 30)
root.mainloop()
