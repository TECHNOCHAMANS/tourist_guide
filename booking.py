from tkinter import *
import webbrowser
import tkinter as tk
from PIL import ImageTk

root = Tk()
root.title('HELP')
root.geometry('700x500')


bg_icon = ImageTk.PhotoImage(file='/home/nidhi/Documents/python mini project/login.jpg')
bg_lbl = Label(root, image=bg_icon).pack()


label = tk.Label(root, text="All Help You Need", font=("", 25, "bold"), bg='black',fg='white')
label.place(x=170, y=40)

new = 1
url1 = "https://www.redbus.in/"

new = 2
url2 = "https://www.irctc.co.in/"

new = 3
url3 = "https://www.makemytrip.com/flights/"

new = 4
url4 = "https://www.makemytrip.com/hotels/"

new = 5
url5 = "https://www.google.com/maps"


def openweb1():
    webbrowser.open(url1, new=new)


def openweb2():
    webbrowser.open(url2, new=new)


def openweb3():
    webbrowser.open(url3, new=new)


def openweb4():
    webbrowser.open(url4, new=new)


def openweb5():
    webbrowser.open(url5, new=new)


Btn1 = tk.Button(root, text="BUS BOOKING", command=openweb1,bg='black',fg='white')
Btn1.place(x=100, y=130)
Btn2 = tk.Button(root, text="TRAIN BOOKING", command=openweb2,bg='black',fg='white')
Btn2.place(x=100, y=200)
Btn3 = tk.Button(root, text="FLIGHT BOOKING", command=openweb3,bg='black',fg='white')
Btn3.place(x=100, y=270)
Btn4 = tk.Button(root, text="HOTEL BOOKING", command=openweb4,bg='black',fg='white')
Btn4.place(x=100, y=340)
Btn5 = tk.Button(root, text="GOOGLE MAPS", command=openweb5,bg='black',fg='white')
Btn5.place(x=100, y=410)
Btn6 = tk.Button(root, text="NEXT",bg='black',fg='white')
Btn6.place(x=600, y=450)
Btn7 = tk.Button(root, text="BACK",bg='black',fg='white')
Btn7.place(x=500, y=450)

root.mainloop()



