from cProfile import label
from cgitb import text
from logging import PlaceHolder
from tkinter import *
import tkinter
from turtle import color
from  OurEncryption import *
from tkinter.font import Font


root = Tk() 
key_var = tkinter.StringVar()
text_var = tkinter.StringVar()
answer = tkinter.StringVar()
def click1():
    txt1 = text_var.get().upper()
    key = key_var.get().replace(" ","").upper()
    answer.set(seperate(txt1,key))
    txt3 = Label(root,textvariable=answer,font=font_3,fg="#0b5e84",background="#fff",borderwidth=10, relief=tkinter.FLAT).place(x = 40,y = 350)
    text_var.set("")
    key_var.set("")

def click2():
    txt1 = text_var.get().upper()
    key = key_var.get().replace(" ","").upper()
    answer.set(seperate_decryption(txt1,key))
    txt3 = Label(root,textvariable=answer,font=font_3,fg="#0b5e84",background="#fff",borderwidth=10, relief=tkinter.FLAT).place(x = 40,y = 350)
    text_var.set("")
    key_var.set("")

root.geometry("512x512")
root.title("Playfair Cipher")
font_3 = Font(family='Nueva Std Cond', size=14, weight='bold', slant='roman', underline=0, overstrike=0)
font_2 = Font(family='Nueva Std Cond', size=12, weight='normal', slant='roman', underline=0, overstrike=0)
txt = Label(root,text = "Enter The Key",font=font_3,fg="#0b5e84").place(x = 40,y = 60) 
entry = Entry(root,width=45,font=font_2,textvariable=key_var,borderwidth=10, relief=tkinter.FLAT,fg="#0b5e84").place(x=40,y=100)
txt1 = Label(root,text = "Enter The Text",font=font_3,fg="#0b5e84").place(x = 40,y = 150) 
entry1 = Entry(root,width=45,font=font_2,textvariable=text_var,borderwidth=10, relief=tkinter.FLAT,fg="#0b5e84").place(x=40,y=190)
btn1 =  Button(root,command=click1,text="encrypt",fg="#fff",bg="#0b5e84",font=font_3).place(x=130,y=260)
btn2 =  Button(root,command=click2,text="decrypt",fg="#fff",bg="#0b5e84",font=font_3).place(x=270,y=260)
#txt3 = Label(root,textvariable=answer,font=font_3,fg="#0b5e84",background="#fff",borderwidth=10, relief=tkinter.FLAT).place(x = 40,y = 350) 


# Code to add widgets will go here...
root.mainloop()