from tkinter import *

root = Tk()
root.geometry("312x324")  # this is for the size of the window 
root.resizable(0, 0)
root.title('Simple Calculator')


def buttonclick(number):
    global exp
    exp = exp + str(number)
    input_text.set(exp)
    #print(str(str1))

def buttonclear():
    global exp 
    exp = "" 
    input_text.set("")

def calculate():
    global exp
    result = str(eval(exp)) # 'eval':This function is used to evaluates the string expression directly
    input_text.set(result)
    exp = ""


exp = ""
input_text = StringVar()

input_frame = Frame(root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side=TOP, padx = 6) 

entry1 = Entry(input_frame, font=('arial', 12), textvariable=input_text, width=40, bg="#eee", bd=0, justify=LEFT)
entry1.grid(row=0, column=0)
entry1.pack(ipady=10)

btns_frame = Frame(root, width=308, height=260, bg="grey") #height=212.5
btns_frame.pack(pady=5)

# first row
 
clear = Button(btns_frame, text = "CLEAR", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", command=buttonclear)
clear.grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
 
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", command=lambda: buttonclick("/"))
divide.grid(row = 0, column = 3, padx = 1, pady = 1)
 
# second row
 
seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", command=lambda: buttonclick(7))
seven.grid(row = 1, column = 0, padx = 1, pady = 1)
 
eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", command=lambda: buttonclick(8))
eight.grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", command=lambda: buttonclick(9))
nine.grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", command=lambda: buttonclick("*"))
multiply.grid(row = 1, column = 3, padx = 1, pady = 1)
 
# third row
 
four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", command=lambda: buttonclick(4))
four.grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", command=lambda: buttonclick(5))
five.grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", command=lambda: buttonclick(6))
six.grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", command=lambda: buttonclick("-"))
minus.grid(row = 2, column = 3, padx = 1, pady = 1)
 
# fourth row
 
one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", command=lambda: buttonclick(1))
one.grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", command=lambda: buttonclick(2))
two.grid(row = 3, column = 1, padx = 1, pady = 1)
 
three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", command=lambda: buttonclick(3))
three.grid(row = 3, column = 2, padx = 1, pady = 1)
 
plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", command=lambda: buttonclick("+"))
plus.grid(row = 3, column = 3, padx = 1, pady = 1)
 
# fourth row
 
zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", command=lambda: buttonclick(0))
zero.grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 
point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", command=lambda: buttonclick("."))
point.grid(row = 4, column = 2, padx = 1, pady = 1)
 
equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", command=calculate)
equals.grid(row = 4, column = 3, padx = 1, pady = 1)


#clear = Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)

root.mainloop()