from tkinter import *
from tkinter import font
from tkinter import ttk 
from turtle import bgcolor, width
from PIL import ImageTk, Image
import customtkinter

simu = Tk()
simu.configure(background='black')
simu.geometry("900x1000") 
simu.title("Overcast")
simu.iconbitmap("logo.ico")

mainframe = Frame(simu)
mainframe.pack(fill=BOTH, expand=1)

mycanvas = Canvas(mainframe)
mycanvas.pack(side=LEFT,fill=BOTH,expand=1)

myscrollbar = ttk.Scrollbar(mainframe,orient=VERTICAL, command=mycanvas.yview)
myscrollbar.pack(side=RIGHT,fill=Y)

mycanvas.configure(yscrollcommand=myscrollbar.set)
mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion=mycanvas.bbox("all")))

secondframe = Frame(mycanvas)
mycanvas.create_window((0,0),window=secondframe, anchor="nw")



for thing in range(100):
    Button(secondframe,text=f'Button{thing} Yo!').grid(row=thing)

simu.mainloop()