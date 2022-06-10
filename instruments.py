from tkinter import *
from tkinter import font
from tkinter import ttk 
from turtle import bgcolor, width
from PIL import ImageTk, Image
import customtkinter

solexptext = "An anemometer is any device that measures wind speed. \nThis design works well because the aerodynamically \ndesigned cups capture the maximum amount of wind force \non the open side while allowing the air to easily flow over\n the back side of the cups turn through their \nrotation. Another quality feature is a dual bearing design that eliminates \nshaft wobble and flex, something not \noffered on other similarly priced weather\n station systems."
latloctext = "A wind vane indicates the direction the wind is blowing.\n Wind vanes are fairly simple devices. A fin sits \non a spindle that can rotate horizontally. Since it’s \nlonger on one end than the other, the fin will always point\n in the direction the wind is blowing."
airptext = "A barometer measures atmospheric pressure. \nIt uses a piezo-resistive pressure sensor, which converts \natmospheric pressure into an analog electrical signal. The way \nit works is that the pressure sensor contains what is known \nas a strain gauge. Strain gauges used for this \npurpose are often made in the form of a diaphragm. The greater the \natmospheric pressure, the more the diaphragm \nwill deform. "
waterptext = "Incredibly simple, easy-to-use and economical, \nthese devices collect raindrops during a storm and \n(via graduated lines) tell you how many inches of rain has fallen. \nTypically, analog rain gauges top out at around five inches\n and will need to periodically be emptied to \ncontinually measure a rainfall that exceeds their liquid capacity. \nThey will also need to be manually emptied between \nrain events to obtain an \naccurate measurement of a subsequent storm."

facts = Tk()
facts.configure(background='black')
facts.geometry("1600x1000") 
facts.title("Overcast")
facts.iconbitmap("logo.ico")

mainframe = Frame(facts)
mainframe.pack(fill=BOTH, expand=1)

mycanvas = Canvas(mainframe)
mycanvas.pack(side=LEFT,fill=BOTH,expand=1)

myscrollbar = ttk.Scrollbar(mainframe,orient=VERTICAL, command=mycanvas.yview)
myscrollbar.pack(side=RIGHT,fill=Y)

mycanvas.configure(yscrollcommand=myscrollbar.set,background="black")
mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion=mycanvas.bbox("all")))

secondframe = Frame(mycanvas,background="black")
mycanvas.create_window((0,0),window=secondframe, anchor="nw")

factors = Label(secondframe, text="Instruments used for Weather Forcasting",
font=("Arial", 25),
bg="black",
fg="white").pack()
img = ImageTk.PhotoImage(Image.open("logo.png"))
panel = Label(secondframe, image = img, bg="black").pack()

spacer1 = Label(secondframe,bg = "black", text="\n")
spacer1.pack()

sol = Label(secondframe, text="Anemometers",
font=("Arial", 25),
bg="black",
fg="white").pack()

solexp = Label(secondframe, text=solexptext,
font=("Arial", 15),
bg="black",
fg="white").pack()

img1 = ImageTk.PhotoImage(Image.open("ins1.jpg"))
panel1 = Label(secondframe, image = img1, bg="black").pack()

spacer1 = Label(secondframe,bg = "black", text="\n")
spacer1.pack()

latloc = Label(secondframe, text="Wind vane",
font=("Arial", 25),
bg="black",
fg="white").pack()

solexp = Label(secondframe, text=latloctext,
font=("Arial", 15),
bg="black",
fg="white").pack()

img2 = ImageTk.PhotoImage(Image.open("ins2.jpg"))
panel2 = Label(secondframe, image = img2, bg="black").pack()

spacer1 = Label(secondframe,bg = "black", text="\n")
spacer1.pack()

sol = Label(secondframe, text="Barometers",
font=("Arial", 25),
bg="black",
fg="white").pack()

solexp = Label(secondframe, text=airptext,
font=("Arial", 15),
bg="black",
fg="white").pack()

img3 = ImageTk.PhotoImage(Image.open("ins5.jpg"))
panel3 = Label(secondframe, image = img3, bg="black").pack()

spacer1 = Label(secondframe,bg = "black", text="\n")
spacer1.pack()

sol = Label(secondframe, text="Rain Gauages",
font=("Arial", 25),
bg="black",
fg="white").pack()

solexp = Label(secondframe, text=waterptext,
font=("Arial", 15),
bg="black",
fg="white").pack()

img4 = ImageTk.PhotoImage(Image.open("ins4.jpg"))
panel4 = Label(secondframe, image = img4, bg="black").pack()

facts.mainloop()