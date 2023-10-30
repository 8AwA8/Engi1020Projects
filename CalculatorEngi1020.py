from tkinter import *
from tkinter import font
import tkinter as tk
import math
from PIL import Image, ImageTk


def Multiply():
    return(round(float(n1.get())*float(n2.get()), 4))

def Divide():
    return(round(float(n1.get())/float(n2.get()), 4))

def Add():
    return(round(float(n1.get())+float(n2.get()), 4))

def Subtract():
    return(round(float(n1.get())-float(n2.get()), 4))

def Power():
    return(round(float(n1.get())**float(n2.get()), 4))

def Root():
    return(round(float(n1.get())**(1/float(n2.get())), 4))


def OpFinder():
    print(n1.get(), n2.get())
    if menu.get() == ops[0]:
        otx.config(text = Add())
    elif menu.get() == ops[1]:
        otx.config(text = Subtract())
    elif menu.get() == ops[2]:
        otx.config(text = Multiply())
    elif menu.get() == ops[3]:
        otx.config(text = Divide())
    elif menu.get() == ops[4]:
        otx.config(text = Power())
    elif menu.get() == ops[5]:
        otx.config(text = Root())
    else:
        print("Something Went Wrond")

def OpReCol(R):
    if R == ops[0]:
        odr.config(background='#5322DA', activebackground='#5322DA')
    elif R == ops[1]:
        odr.config(background='#AF22DA', activebackground='#AF22DA')
    elif R == ops[2]:
        odr.config(background='#DA22A9', activebackground='#DA22A9')
    elif R == ops[3]:
        odr.config(background='#DA224D', activebackground='#DA224D')
    elif R == ops[4]:
        odr.config(background='#DA5322', activebackground='#DA5322')
    elif R == ops[5]:
        odr.config(background='#DAAF22', activebackground='#DAAF22')


calcw = tk.Tk()

times50 = font.Font(family='times new roman', size = 80)
times20 = font.Font(family='times new roman', size = 20, weight="bold")
times25 = font.Font(family='times new roman', size = 25, weight="bold", underline=TRUE)

ops = ["Plus", "Minus", "Multiplied By", "Divided By", "To The Power Of", "To The Root Of"]

'''Background creation'''
bgfile = Image.open("CalcBg.png")
bgfile = bgfile.resize((1960,1280))
bgn = ImageTk.PhotoImage(bgfile)
bg = Label(calcw, image=bgn)
bg.place(x=-5, y=-5)

wtx = Label(calcw, text="Calculator", fg="#FFFFFF",anchor=CENTER, background="#000000", font=times50)
wtx.pack(pady=(50,0))

n1tx = Label(calcw, text="First Number", fg="#FFFFFF",anchor=CENTER, background="#000000", font=times20)
n1tx.pack(pady=(100,0))

n1 = tk.Entry(calcw)
n1.config(font=times20)
n1.pack()

menu = StringVar()
menu.set("Plus")
odr = OptionMenu(calcw, menu, *ops, command=OpReCol)
odr.config(font=times20,background='#5322DA', activebackground='#5322DA')
odr.pack(pady=(50,30))

n2tx = Label(calcw, text="Second Number", fg="#FFFFFF",anchor=CENTER, background="#000000", font=times20)
n2tx.pack()

n2 = tk.Entry(calcw)
n2.config(font=times20)
n2.pack()

conf = Button(calcw, text="Run Calculation", font=times20, bg="#DA4222", activebackground='#22DA9E', command=OpFinder)
conf.pack(pady=(100,0))

otx = Label(calcw, text="Output", fg="#FFFFFF",anchor=CENTER, background="#000000", font=times25)
otx.pack(pady=50)

calcw.mainloop()