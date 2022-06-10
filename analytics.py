from tkinter import *
from tkinter import font
from tkinter import ttk 
from turtle import bgcolor, width
from PIL import ImageTk, Image
import customtkinter

solexptext = "Weather models are at the heart and they are \nused both for forecasting and to recreate historical data. \nHowever, over the last decade, machine learning has increasingly come to \nbe applied in atmospheric science. Machine learning takes weather \ndata and builds relationships between the available data and the \nrelative predictors. ML can help improve physically grounded models, \nand by combining both approaches, they can get accurate results. \nSophisticated models and ML are used to forecast the weather using \na combination of physical models and measured \ndata on huge computer systems."
latloctext = "It is necessary to have the right data to be\n close to accurate decisions. The data needs to be taken with \nrespect to the location and the time at which it is noted has to be considered. \nToday, all the devices are IoT-enabled with gyrometer, \nbarometers and all sorts of sensors in it. So, the location from one \nstandpoint to another is very well available. Therefore, mobile phones\n proved to be revolutionizing the analytics weather industry and \nthey have really changed the industry."
airptext = "Today, the primary source of atmospheric science \nis satellite imagery and that does not mean pretty pictures though! \nSatellite imagery comes in different sizes and shapes. Some satellites\n operate in the black and white spectrum, some can be useful \nto identify and measure clouds, others to measure winds over the \noceans. Most data scientists rely on satellite imagery to generate short\n term forecasts, to determine whether a forecast is correct, and\n to validate models too. Machine learning is also used here for \npattern matching. If it acknowledges a pattern\n that has already appeared in the past, it can be used to predict what is going to happen in the future."

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

factors = Label(secondframe, text="Analytics used for Weather Forcasting",
font=("Arial", 25),
bg="black",
fg="white").pack()
img = ImageTk.PhotoImage(Image.open("logo.png"))
panel = Label(secondframe, image = img, bg="black").pack()

spacer1 = Label(secondframe,bg = "black", text="\n")
spacer1.pack()

sol = Label(secondframe, text="Predictive Modeling and Machine Learning",
font=("Arial", 25),
bg="black",
fg="white").pack()

solexp = Label(secondframe, text=solexptext,
font=("Arial", 15),
bg="black",
fg="white").pack()
spacer1 = Label(secondframe,bg = "black", text="\n")
spacer1.pack()

latloc = Label(secondframe, text="Data – A Crucial Part of Weather Predictions",
font=("Arial", 25),
bg="black",
fg="white").pack()

solexp = Label(secondframe, text=latloctext,
font=("Arial", 15),
bg="black",
fg="white").pack()

spacer1 = Label(secondframe,bg = "black", text="\n")
spacer1.pack()

sol = Label(secondframe, text="Satellite Imagery and Sensor Data",
font=("Arial", 25),
bg="black",
fg="white").pack()

solexp = Label(secondframe, text=airptext,
font=("Arial", 15),
bg="black",
fg="white").pack()

spacer1 = Label(secondframe,bg = "black", text="\n")
spacer1.pack()

img4 = ImageTk.PhotoImage(Image.open("sat1.jpg"))
panel4 = Label(secondframe, image = img4, bg="black").pack()

facts.mainloop()