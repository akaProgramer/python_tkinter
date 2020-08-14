
# from functools import partial
# from tkinter import *

# root = Tk()

# def key(event):
#     print ("pressed"), repr(event.char)
#     if event.char.isdigit():
#         append_digit(event.char)
#     elif event.char in ('\x08', '\x7f'):
#         backspace()

# def callback(event):
#     frame.focus_set()
#     print ("clicked at", event.x, event.y)

# frame = Frame(root, width=100, height=100)
# frame.bind("<Key>", key)
# frame.bind("<Button-1>", callback)
# frame.pack()

# current = IntVar(0)
# label = Label(frame, textvariable=current)
# label.pack()

# def button_callback(i):
#     print ("clicked button {}".format(i))
#     append_digit(i)

# def append_digit(digit):
#     current.set(current.get() * 10 + int(digit))

# def backspace():
#     current.set(current.get() // 10)

# for i in '1234567890':
#     Button(frame, text=i, command=partial(button_callback, i)).pack()
# Button(frame, text='C', command=backspace).pack()

# frame.focus_set()
# root.mainloop()
#-*-coding: utf-8-*-
# from tkinter import *
# import math

# class calc:
#  def getandreplace(self):
#   """replace x with * and ÷ with /"""
  
#   self.expression = self.e.get()
#   self.newtext=self.expression.replace(self.newdiv,'/')
#   self.newtext=self.newtext.replace('x','*')

#  def equals(self):
#   """when the equal button is pressed"""

#   self.getandreplace()
#   try: 
#    self.value= eval(self.newtext) #evaluate the expression using the eval function
#   except SyntaxError or NameErrror:
#    self.e.delete(0,END)
#    self.e.insert(0,'Invalid Input!')
#   else:
#    self.e.delete(0,END)
#    self.e.insert(0,self.value)
 
#  def squareroot(self):
#   """squareroot method"""
  
#   self.getandreplace()
#   try: 
#    self.value= eval(self.newtext) #evaluate the expression using the eval function
#   except SyntaxError or NameErrror:
#    self.e.delete(0,END)
#    self.e.insert(0,'Invalid Input!')
#   else:
#    self.sqrtval=math.sqrt(self.value)
#    self.e.delete(0,END)
#    self.e.insert(0,self.sqrtval)

#  def square(self):
#   """square method"""
  
#   self.getandreplace()
#   try: 
#    self.value= eval(self.newtext) #evaluate the expression using the eval function
#   except SyntaxError or NameErrror:
#    self.e.delete(0,END)
#    self.e.insert(0,'Invalid Input!')
#   else:
#    self.sqval=math.pow(self.value,2)
#    self.e.delete(0,END)
#    self.e.insert(0,self.sqval)
 
#  def clearall(self): 
#   """when clear button is pressed,clears the text input area"""
#   self.e.delete(0,END)
 
#  def clear1(self):
#   self.txt=self.e.get()[:-1]
#   self.e.delete(0,END)
#   self.e.insert(0,self.txt)

#  def action(self,argi): 
#   """pressed button's value is inserted into the end of the text area"""
#   self.e.insert(END,argi)
 
#  def __init__(self,master):
#   """Constructor method"""
#   master.title('Calulator') 
#   master.geometry()
#   self.e = Entry(master)
#   self.e.grid(row=0,column=0,columnspan=6,pady=3)
#   self.e.focus_set() #Sets focus on the input text area
    
#   self.div='÷'
#   self.newdiv=self.div.decode('utf-8')

#   #Generating Buttons
#   Button(master,text="=",width=10,command=lambda:self.equals()).grid(row=4, column=4,columnspan=2)
#   Button(master,text='AC',width=3,command=lambda:self.clearall()).grid(row=1, column=4)
#   Button(master,text='C',width=3,command=lambda:self.clear1()).grid(row=1, column=5)
#   Button(master,text="+",width=3,command=lambda:self.action('+')).grid(row=4, column=3)
#   Button(master,text="x",width=3,command=lambda:self.action('x')).grid(row=2, column=3)
#   Button(master,text="-",width=3,command=lambda:self.action('-')).grid(row=3, column=3)
#   Button(master,text="÷",width=3,command=lambda:self.action(self.newdiv)).grid(row=1, column=3) 
#   Button(master,text="%",width=3,command=lambda:self.action('%')).grid(row=4, column=2)
#   Button(master,text="7",width=3,command=lambda:self.action('7')).grid(row=1, column=0)
#   Button(master,text="8",width=3,command=lambda:self.action(8)).grid(row=1, column=1)
#   Button(master,text="9",width=3,command=lambda:self.action(9)).grid(row=1, column=2)
#   Button(master,text="4",width=3,command=lambda:self.action(4)).grid(row=2, column=0)
#   Button(master,text="5",width=3,command=lambda:self.action(5)).grid(row=2, column=1)
#   Button(master,text="6",width=3,command=lambda:self.action(6)).grid(row=2, column=2)
#   Button(master,text="1",width=3,command=lambda:self.action(1)).grid(row=3, column=0)
#   Button(master,text="2",width=3,command=lambda:self.action(2)).grid(row=3, column=1)
#   Button(master,text="3",width=3,command=lambda:self.action(3)).grid(row=3, column=2)
#   Button(master,text="0",width=3,command=lambda:self.action(0)).grid(row=4, column=0)
#   Button(master,text=".",width=3,command=lambda:self.action('.')).grid(row=4, column=1)
#   Button(master,text="(",width=3,command=lambda:self.action('(')).grid(row=2, column=4)
#   Button(master,text=")",width=3,command=lambda:self.action(')')).grid(row=2, column=5)
#   Button(master,text="√",width=3,command=lambda:self.squareroot()).grid(row=3, column=4)
#   Button(master,text="x²",width=3,command=lambda:self.square()).grid(row=3, column=5)
# #Main
# root = Tk()
# obj=calc(root) #object instantiated
# root.mainloop()


# from tkinter import *
# from math import *

# root = Tk()
# root.title("Calculator")
# root.resizable(width=False, height=False)

# screen = StringVar()
# screen.set("0")

# current = ""
# power = ""

# firstnum = str()
# secondnum = str()
# mathsign = str()

# defxworking = False
# percentt = False

# def math_button_pressed():
#     if mathsign == '+':
#         button_plus.config(relief=SUNKEN)
#     if mathsign == '-':
#         button_minus.config(relief=SUNKEN)
#     if mathsign == '*':
#         button_multiply.config(relief=SUNKEN)
#     if mathsign == '/':
#         button_division.config(relief=SUNKEN)

# def math_button_raised():
#     button_plus.config(relief=RAISED)
#     button_minus.config(relief=RAISED)
#     button_multiply.config(relief=RAISED)
#     button_division.config(relief=RAISED)

# def is_int(num):
#     if int(num) == float(num):
#         return int(num)
#     else:
#         return float(num)

# def number_pressed(butt):
#     global current, power, firstnum, secondnum

#     if mathsign == str() and defxworking == False:
#         current = current + str(butt)
#         screen.set(current)
#         firstnum = float(current)

#     elif mathsign != str() and defxworking == False:
#         math_button_raised()
#         current = current + str(butt)
#         screen.set(current)
#         secondnum = float(current)

#     elif mathsign == str() and defxworking == True:
#         power = power + str(butt)
#         current = current + str(butt)
#         screen.set(current)

#     elif mathsign != str and defxworking == True:
#         power = power + str(butt)
#         current = current + str(butt)
#         screen.set(current)
#         print(power)

# def math_pressed(math):
#     global current, power, mathsign, firstnum, secondnum, defxworking, percentt

#     if mathsign == str() and defxworking == False and percentt == False and firstnum != str():
#         mathsign = str(math)
#         math_button_pressed()
#         current = ""

#     elif mathsign != str() and defxworking == False and percentt == False:
#         print(2)
#         if mathsign == '+':
#             firstnum = round(float(firstnum + secondnum),6)
#         if mathsign == '-':
#             firstnum = round(float(firstnum - secondnum),6)
#         if mathsign == '*':
#             firstnum = round(float(firstnum * secondnum),6)
#         if mathsign == '/':
#             firstnum = round(float(firstnum / secondnum),6)
#         screen.set(is_int(firstnum))

#         mathsign = str(math)
#         math_button_pressed()
#         current = ""

#     elif mathsign != str() and defxworking == True and percentt == False:
#         if mathsign == '+':
#             firstnum = round(firstnum + secondnum ** int(power),6)
#         if mathsign == '-':
#             firstnum = round(firstnum - secondnum ** int(power),6)
#         if mathsign == '*':
#             firstnum = round(firstnum * (secondnum ** int(power)),6)
#         if mathsign == '/':
#             firstnum = round(firstnum / (secondnum ** int(power)),6)
#         defxworking = False
#         screen.set(is_int(firstnum))
#         defxworking = False
#         mathsign = str(math)
#         math_button_pressed()
#         power = ""
#         current = ""

#     elif defxworking and percentt == False:
#         firstnum = round(firstnum ** int(power), 6)
#         defxworking = False
#         screen.set(is_int(firstnum))
#         mathsign = str(math)
#         math_button_pressed()
#         power = ""
#         current = ""

#     elif percentt:
#         if mathsign == '+':
#             firstnum = round(float(firstnum + firstnum/100*secondnum),6)
#         if mathsign == '-':
#             firstnum = round(float(firstnum - firstnum/100*secondnum),6)
#         screen.set(is_int(firstnum))
#         percentt = False
#         mathsign = str(math)
#         math_button_pressed()
#         current = ""

# def squareroot():
#     global firstnum, secondnum, mathsign, current

#     if mathsign == str():
#         firstnum = round(sqrt(firstnum),6)
#         screen.set(is_int(firstnum))

#     if mathsign != str():
#         if mathsign == '+':
#             firstnum = round(sqrt(firstnum + float(secondnum)),6)
#         if mathsign == '-':
#             firstnum = round(sqrt(firstnum - float(secondnum)),6)
#         if mathsign == '*':
#             firstnum = round(sqrt(firstnum * float(secondnum)),6)
#         if mathsign == '/':
#             firstnum = round(sqrt(firstnum / float(secondnum)),6)

#         screen.set(is_int(firstnum))
#         secondnum = str()
#         mathsign = str()
#         current = ""

# def x():
#     global firstnum, secondnum, mathsign, current, defxworking

#     if mathsign == str():
#         current = str(is_int(firstnum)) + '^'
#         screen.set(current)
#         defxworking = True

#     elif mathsign != str():

#         current = str(is_int(secondnum)) + '^'
#         screen.set(current)
#         defxworking = True

# def result():
#     global firstnum, secondnum, mathsign, current, power, defxworking, percentt
#     if defxworking == False and percentt == False:
#         if mathsign == '+':
#             firstnum = round(float(firstnum + secondnum),6)
#         if mathsign == '-':
#             firstnum = round(float(firstnum - secondnum),6)
#         if mathsign == '*':
#             firstnum = round(float(firstnum * secondnum),6)
#         if mathsign == '/':
#             firstnum = round(float(firstnum / secondnum),6)
#         screen.set(is_int(firstnum))

#     if mathsign == str() and defxworking == True and percentt == False:
#         firstnum = round(firstnum ** int(power),6)
#         defxworking = False
#         screen.set(is_int(firstnum))

#     if mathsign != str() and defxworking == True and percentt == False:
#         if mathsign == '+':
#             firstnum = round(firstnum + secondnum ** int(power),6)
#             defxworking = False
#         if mathsign == '-':
#             firstnum = round(firstnum - secondnum ** int(power),6)
#             defxworking = False
#         if mathsign == '*':
#             firstnum = round(firstnum * (secondnum ** int(power)),6)
#             defxworking = False
#         if mathsign == '/':
#             firstnum = round(firstnum / (secondnum ** int(power)),6)
#             defxworking = False
#         screen.set(is_int(firstnum))


#     if defxworking == False and percentt == True:
#         if mathsign == '+':
#             firstnum = round(float(firstnum + firstnum/100*secondnum),6)
#             screen.set(is_int(firstnum))
#             percentt = False
#         if mathsign == '-':
#             firstnum = round(float(firstnum - firstnum/100*secondnum),6)
#             screen.set(is_int(firstnum))
#             percentt = False

#     mathsign = str()
#     current = ""
#     power = ""

#     if defxworking == False and mathsign == '*' or '/' and percentt == True:
#         clear()

# def clear():
#     global current, firstnum, secondnum, mathsign, power, defxworking, percentt

#     screen.set(0)
#     current = ""
#     power = ""
#     firstnum = str()
#     secondnum = str()
#     mathsign = str()
#     defxworking = False
#     math_button_raised()
#     percentt = False

# def percent():
#     global firstnum, secondnum, current, percentt

#     current = str(is_int(secondnum)) + '%'
#     screen.set(current)
#     percentt = True



# # Widgets

# calculation = Entry(root, textvariable = screen, font=("Verdana", 15, ), bd = 12,
#                     insertwidth=4, width=14, justify=RIGHT)
# calculation.grid(columnspan=4)
# #   Numbers
# button1 = Button(root, text='1', command=lambda: number_pressed(1), bg="gainsboro",
#                  bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
# button1.grid(row=2, column=0, sticky=W)
# button2 = Button(root, text='2', command=lambda: number_pressed(2), bg="gainsboro",
#                  bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
# button2.grid(row=2, column=1, sticky=W)
# button3 = Button(root, text='3', command=lambda: number_pressed(3), bg="gainsboro",
#                  bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
# button3.grid(row=2, column=2, sticky=W)
# button4 = Button(root, text='4', command=lambda: number_pressed(4), bg="gainsboro",
#                  bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
# button4.grid(row=3, column=0, sticky=W)
# button5 = Button(root, text='5', command=lambda: number_pressed(5), bg="gainsboro",
#                  bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
# button5.grid(row=3, column=1, sticky=W)
# button6 = Button(root, text='6', command=lambda: number_pressed(6), bg="gainsboro",
#                  bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
# button6.grid(row=3, column=2, sticky=W)
# button7 = Button(root, text='7', command=lambda: number_pressed(7), bg="gainsboro",
#                  bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
# button7.grid(row=4, column=0, sticky=W)
# button8 = Button(root, text='8', command=lambda: number_pressed(8), bg="gainsboro",
#                  bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
# button8.grid(row=4, column=1, sticky=W)
# button9 = Button(root, text='9', command=lambda: number_pressed(9), bg="gainsboro",
#                  bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
# button9.grid(row=4, column=2, sticky=W)
# button0 = Button(root, text='0', command=lambda: number_pressed(0), bg="gainsboro",
#                  bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
# button0.grid(row=5, column=0, sticky=W)
# button_float = Button(root, text='.', command=lambda: number_pressed('.'), bg="gainsboro",
#                       bd=3, padx=15, pady=5, font=("Helvetica", 14, "bold"))
# button_float.grid(row=5, column=1)

# #   Math signs
# button_plus = Button(root, text='+', command=lambda: math_pressed('+'), bg="gray70",
#                      bd=3, padx=11, pady=5, font=("Helvetica", 14, "bold"))
# button_plus.grid(row=2, column=3, sticky=W)
# button_minus = Button(root, text='-', command=lambda: math_pressed('-'),  bg="gray70",
#                       bd=3, padx=11, pady=4, font=("Verdana", 14, "bold"))
# button_minus.grid(row=3, column=3, sticky=W)
# button_multiply = Button(root, text='*', command=lambda: math_pressed('*'), bg="gray70",
#                          bd=3, padx=13, pady=5, font=("Helvetica", 14, "bold"))
# button_multiply.grid(row=4, column=3, )
# button_division = Button(root, text='/', command=lambda: math_pressed('/'),  bg="gray70",
#                          bd=3, padx=14, pady=5, font=("Helvetica", 14, "bold"))
# button_division.grid(row=5, column=3, )
# button_equal = Button(root, text='=', command=lambda: result(), bg='orange',
#                       bd=3, padx=12, pady=5, font=("Arial", 14))
# button_equal.grid(row=5, column=2, )

# button_percent = Button(root, text='%', command=lambda: percent(),  bg="gray70",
#                          bd=3, padx=8, pady=5, font=("Helvetica", 14, "bold"))
# button_percent.grid(row=1, column=3, )

# button_clear = Button(root, text='C', command=lambda: clear(), bg='gray70',
#                       bd=3, padx=11, pady=5, font=("Helvetica", 14))
# button_clear.grid(row=1, column=0)
# button_sqrt = Button(root, text='√', command=lambda: squareroot(), bg="gray70",
#                         bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
# button_sqrt.grid(row=1, column=1, sticky=W)
# button_x = Button(root, text='x^y', command=lambda: x(), bg="gray70",
#                   bd=3, padx=6, pady=5, font=("Helvetica", 14))
# button_x.grid(row=1, column=2, sticky=W)

# root.mainloop()
from tkinter import Tk,Button,Entry,StringVar
import re

def check(inp):
    try:
        int(inp)
    except ValueError:
        return False
    else:
        return True
def click(event):
    text = var.get()

    if not check(text):
        var.set(re.sub("\D", "", text))  # Remove non-digits

root=Tk()
root.geometry("400x400")
var=StringVar()
entry= Entry(root,textvar=var)
entry.pack()

root.bind("<Key>",lambda event: click(event))
root.mainloop()