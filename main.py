from tkinter import *
from tkinter import font
from turtle import bgcolor, onclick, width
from PIL import ImageTk, Image
import customtkinter
from tkinter import ttk

def factorscall():
    root.destroy()
    import factors


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")
root = Tk()
root.configure(background='black')
root.geometry("900x1000") 
root.title("Overcast")
root.iconbitmap("logo.ico")

img = ImageTk.PhotoImage(Image.open("logo.png"))
panel = Label(root, image = img, bg="black").pack()

Label(root, text="Learn How Weather Forcasting is Done",
font=("Arial", 25),
bg="black",
fg="white").pack()

spacer1 = Label(root,bg = "black", text="\n")
spacer1.pack()

frame_1 = customtkinter.CTkFrame(master=root,
 width = 1100,
 height = 300,
 bg = "grey",
 corner_radius=15)
frame_1.pack()
# button = customtkinter.CTkButton(text="LMAOs",
#  corner_radius=10,
#  width=130, height=70, border_width=3,
# #  font=("Arial", 25),
#  hover_color="gray25").pack()

# b = customtkinter.CTkButton(master=frame_1,text="Add Folder",
#  width=190, height=40,
#  compound="right").pack()
button_1 = customtkinter.CTkButton(master=frame_1, text="Factors", width=700, height=40,
                                   compound="right", command=factorscall)

button_1.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

button_2 = customtkinter.CTkButton(master=frame_1,  text="Instruments", width=700, height=40,
                                   compound="right", fg_color="#D35B58", hover_color="#C77C78")
button_2.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

button_3 = customtkinter.CTkButton(master=frame_1, text="Analytics", width=700, height=40,
                                   compound="right")

button_3.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="ew")


spacer2 = Label(root,bg = "black", text="\n")
spacer2.pack()
img1 = ImageTk.PhotoImage(Image.open("mountain.jpg"),width=1000)
panel = Label(root, image = img1).pack()

root.mainloop()