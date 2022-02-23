import tkinter as tk
from tkinter import *

n1 = ""
n2 = ""
index = 0
operator = ""
ansIn = False


def do_math(x,y,op):
    global cscreen, n1, n2, operator, index, ansIn

    number = 0

    if op  == "/":
        number = x/y
    if op  == "*":
        number = x*y
    if op  == "-":
        number = x-y
    if op  == "+":
        number = x+y

    cscreen.tag_configure("right", justify='right')
    cscreen.delete('1.0', END)
    cscreen.insert("1.0", number)
    cscreen.tag_add("right", "1.0", "end")

    n2 = ""
    operator = ""
    n1 = str(number)
    index = 0
    ansIn = True

def change_var(num):
    global n1, n2, cscreen, operator
    if index == 0:
        n1 = n1 + str(num)
        cscreen.tag_configure("right", justify='right')
        cscreen.delete('1.0', END)
        cscreen.insert("1.0", n1)
        cscreen.tag_add("right", "1.0", "end")
        
    elif index == 1:
        n2 = n2 + str(num)
        cscreen.tag_configure("right", justify='right')
        cscreen.delete('1.0', END)
        cscreen.insert("1.0", n1)
        cscreen.insert("1.0", operator)
        cscreen.insert("1.0", n2)
        cscreen.tag_add("right", "1.0", "end")
    
def oper_hit(oper):
    global index,operator,cscreen
    if n1 != "":
        operator = oper
        index += 1
        cscreen.tag_configure("right", justify='right')
        cscreen.insert("1.0", operator)
        cscreen.tag_add("right", "1.0", "end")

def clear(com):
    global cscreen, n1, n2, operator, index

    if com == "c":
        n1 = ""
        n2 = ""
        index = 0
        operator = ""

        cscreen.delete('1.0', END)
        cscreen.pack()
    else:
        text = cscreen.get("1.0", END)
        text = text[1:]
        cscreen.tag_configure("right", justify='right')
        cscreen.delete('1.0', END)
        cscreen.insert("1.0", text)
        cscreen.tag_add("right", "1.0", "end")

        if operator == "" and n2 == "":
            n1 = n1[:-1]
        elif operator != "" and n2 != "":
            n2 = n2[:-1]
        elif n2 == "" and operator != "":
            operator = ""
            index = 0
            

calc = tk.Tk()
calc.geometry("350x500")

cscreen = Text(calc, width=21, height=1, font=("Terminal", 32))
cscreen.tag_configure("right", justify='right')
cscreen.insert("1.0", "")
cscreen.tag_add("right", "1.0", "end")
cscreen.pack()

b1 = tk.Button(calc, text="1", width=7, height=3, command= lambda *args: change_var(1))
b1.place(relx=0.05, rely=0.1)

b2 = tk.Button(calc, text="2", width=7, height=3, command= lambda *args: change_var(2))
b2.place(relx=0.25, rely=0.1)

b3 = tk.Button(calc, text="3", width=7, height=3, command= lambda *args: change_var(3))
b3.place(relx=0.45, rely=0.1)

b4 = tk.Button(calc, text="4", width=7, height=3, command= lambda *args: change_var(4))
b4.place(relx=0.05, rely=0.27)

b5 = tk.Button(calc, text="5", width=7, height=3, command= lambda *args: change_var(5))
b5.place(relx=0.25, rely=0.27)

b6 = tk.Button(calc, text="6", width=7, height=3, command= lambda *args: change_var(6))
b6.place(relx=0.45, rely=0.27)

b7 = tk.Button(calc, text="7", width=7, height=3, command= lambda *args: change_var(7))
b7.place(relx=0.05, rely=0.44)

b8 = tk.Button(calc, text="8", width=7, height=3, command= lambda *args: change_var(8))
b8.place(relx=0.25, rely=0.44)

b9 = tk.Button(calc, text="9", width=7, height=3, command= lambda *args: change_var(9))
b9.place(relx=0.45, rely=0.44)

b0 = tk.Button(calc, text="0", width=7, height=3, command= lambda *args: change_var(0))
b0.place(relx=0.05, rely=0.58)

bd = tk.Button(calc, text=".", width=7, height=3, command= lambda *args: change_var("."))
bd.place(relx=0.25, rely=0.58)

bx = tk.Button(calc, text="X", width=7, height=3, command= lambda *args: clear("x"))
bx.place(relx=0.45, rely=0.58)

clearb = tk.Button(calc, text="C", width=15, height=3, command= lambda *args: clear("c"))
clearb.place(relx=0.65, rely=0.1)

divb = tk.Button(calc, text="/", width=15, height=3, command= lambda *args: oper_hit("/"))
divb.place(relx=0.65, rely=0.22)

mulb = tk.Button(calc, text="*", width=15, height=3, command= lambda *args: oper_hit("*"))
mulb.place(relx=0.65, rely=0.34)

subb = tk.Button(calc, text="-", width=15, height=3, command= lambda *args: oper_hit("-"))
subb.place(relx=0.65, rely=0.46)

addb = tk.Button(calc, text="+", width=15, height=3, command= lambda *args: oper_hit("+"))
addb.place(relx=0.65, rely=0.58)

epb = tk.Button(calc, text="=", width=50, height=5, command= lambda *args: do_math(int(n1) if "." not in n1 else float(n1), int(n2) if "." not in n2 else float(n2), operator))
epb.place(relx=0, rely=0.75)

calc.mainloop()