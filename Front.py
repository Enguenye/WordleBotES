from tkinter import *
from tkinter import ttk
import tkinter as tk
import pandas as pd
import numpy as np
import math
from wordleWithoutFirstWord import removeArray
from wordleWithoutFirstWord import thread_function


class SampleObj():

    def __init__(self):
        self.colores=['grey','grey','grey','grey','grey','grey']
        self.listp=[0,0,0,0,0]
        self.word="PARES"
        df = pd.read_excel('./Lista5Palabrasespa.xlsx')
        self.list2 = df["LIST"].to_numpy()
        self.var="Ingresa la palabra PARES e ingresa la solución:"








def funcbutton(arg,i,info):
    if (info.colores[i]=='grey'):
        info.colores[i]='yellow'
        arg['bg']='yellow'
    elif(info.colores[i]=='yellow'):
        info.colores[i] = 'green'
        arg['bg'] = 'green'
    elif (info.colores[i] == 'green'):
        info.colores[i] = 'grey'
        arg['bg'] = 'grey'

def ok(info):
    for i in range(5):
        if(info.colores[i]=="grey"):
            info.listp[i]=0
        elif(info.colores[i]=="yellow"):
            info.listp[i]=1
        elif(info.colores[i]=="green"):
            info.listp[i]=2
    if (info.listp[0]==2 and info.listp[1]==2 and info.listp[2]==2 and info.listp[3]==2 and info.listp[4]==2):
        label.configure(text="La respuesta es " + info.word)
    else:
        info.list2=removeArray((info.listp[0]), (info.listp[1]), (info.listp[2]), (info.listp[3]), (info.listp[4]),info.word,info.list2)
        print(info.list2)
        info.word=thread_function(info.list2, info.list2)
        print(info.word)
        info.var="Ingresa la palabra " + info.word + " e ingresa la solución"
        label.configure(text=info.var)

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
info=SampleObj()

style = ttk.Style()
style.configure("BW.TLabel", background=info.colores[0])


label=tk.Label(frm, text =info.var)
label.config(font=("Courier", 10))
label.grid(column=3, row=1)
btn=tk.Button(frm, text="1",height = 10, width = 20,font=("Courier", 10))
btn.config(bg=info.colores[0],command=lambda arg=btn:funcbutton(arg,0,info))
btn.grid(column=1, row=2)
btn2=tk.Button(frm, text="2",height = 10, width = 20,font=("Courier", 10))
btn2.config(bg=info.colores[1],command=lambda arg=btn2:funcbutton(arg,1,info))
btn2.grid(column=2, row=2)
btn3=tk.Button(frm, text="3",height = 10, width = 20,font=("Courier", 10))
btn3.config(bg=info.colores[2],command=lambda arg=btn3:funcbutton(arg,2,info))
btn3.grid(column=3, row=2)
btn4=tk.Button(frm, text="4",height = 10, width = 20,font=("Courier", 10))
btn4.config(bg=info.colores[3],command=lambda arg=btn4:funcbutton(arg,3,info))
btn4.grid(column=4, row=2)
btn5=tk.Button(frm, text="5",height = 10, width = 20,font=("Courier", 10))
btn5.config(bg=info.colores[4],command=lambda arg=btn5:funcbutton(arg,4,info))
btn5.grid(column=5, row=2)
ok2=tk.Button(frm, text="Ingresar")
ok2.config(command=lambda :ok(info),height = 10, width = 20,bg="white",font=("Courier", 10))
ok2.grid(column=3, row=3)



root.mainloop()
