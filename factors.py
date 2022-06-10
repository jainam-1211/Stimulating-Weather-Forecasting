from tkinter import *
from tkinter import font
from tkinter import ttk 
from turtle import bgcolor, width
from PIL import ImageTk, Image
import customtkinter

solexptext = "Earth's distance from the sun changes throughout\n its orbit, resulting in up to a \n4 degree Fahrenheit difference between \nthe closest and furthest points. \nThe oscillating tilt of the planet creates\n much larger weather effects, because the tilt\n toward or away from the sun over the course\n of the year determines the amount of\n heat that part of the planet will\n receive. When a hemisphere is tilted toward\n the sun, that part of the planet experiences\n summer, whereas when it is tilted\n away, winter."
latloctext = "Where on Earth you are also affects the weather. \nAt the equator, for instance, \nweather does not change much, because that \nlatitude always receives roughly \nthe same amount of sunlight: around 12 hours \na day. As you move away from the equator, \nhowever, you receive more or less sunlight, \ndepending on the season. Polar regions \nexperience extremely long days in \nsummer and extremely long nights in winter. \nBoth summer and winter temperatures also cool \ngradually as you move north or \nsouth of the equator."
airptext = "Air pressure is influenced by the differences between \nhotter and cooler pockets of air, \nor fronts. When the pockets are very different \nin temperature, they try to mix together, \ncreating movement and pressure. \nWhen they aren’t very different, the atmosphere \nmoves around less -- resulting in, usually, \nfewer weather effects. As air attempts to \nequalize by moving from high pressure \nareas to low pressure areas, this causes wind. \nAdditionally, when pressure is low, air is rising,\n which often means moisture\n accumulation in the atmosphere."
waterptext = "The presence of water has a significant impact on \nweather. Nearby bodies of water \nadd moisture to the atmosphere in the form \nof evaporation, which is why places \nnear oceans or lakes, for instance, are \nusually wetter than the desert. Additionally,\n large bodies of water create winds as \ntemperature differentials between land \nand water send breezes inland during \nthe day and out to sea or onto lakes at night. \nEvaporating water forms different types of \nclouds: cirrus, which are high \nin the atmosphere and made of ice, \nstratus, which form lower down and consist \nof a thick, white blanket of rain drops, and cumulonimbus, \nwhich pile high and signal harsh weather, such as thunder, \nlightning, hail and tornadoes."

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

factors = Label(secondframe, text="Factors Affecting Weather Forcasting",
font=("Arial", 25),
bg="black",
fg="white").pack()
img = ImageTk.PhotoImage(Image.open("logo.png"))
panel = Label(secondframe, image = img, bg="black").pack()

spacer1 = Label(secondframe,bg = "black", text="\n")
spacer1.pack()

sol = Label(secondframe, text="Solar Distance",
font=("Arial", 25),
bg="black",
fg="white").pack()

solexp = Label(secondframe, text=solexptext,
font=("Arial", 15),
bg="black",
fg="white").pack()

img1 = ImageTk.PhotoImage(Image.open("fact1.jpg"))
panel1 = Label(secondframe, image = img1, bg="black").pack()

spacer1 = Label(secondframe,bg = "black", text="\n")
spacer1.pack()

latloc = Label(secondframe, text="Latitude Location",
font=("Arial", 25),
bg="black",
fg="white").pack()

solexp = Label(secondframe, text=latloctext,
font=("Arial", 15),
bg="black",
fg="white").pack()

img2 = ImageTk.PhotoImage(Image.open("fact2.jpg"))
panel2 = Label(secondframe, image = img2, bg="black").pack()

spacer1 = Label(secondframe,bg = "black", text="\n")
spacer1.pack()

sol = Label(secondframe, text="Air Pressure",
font=("Arial", 25),
bg="black",
fg="white").pack()

solexp = Label(secondframe, text=airptext,
font=("Arial", 15),
bg="black",
fg="white").pack()

img3 = ImageTk.PhotoImage(Image.open("facts3.png"))
panel3 = Label(secondframe, image = img3, bg="black").pack()

spacer1 = Label(secondframe,bg = "black", text="\n")
spacer1.pack()

sol = Label(secondframe, text="Water Presence",
font=("Arial", 25),
bg="black",
fg="white").pack()

solexp = Label(secondframe, text=waterptext,
font=("Arial", 15),
bg="black",
fg="white").pack()

img4 = ImageTk.PhotoImage(Image.open("facts4.jpg"))
panel4 = Label(secondframe, image = img4, bg="black").pack()

facts.mainloop()