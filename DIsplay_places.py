from tkinter import *
import webbrowser
import tkinter as tk
from PIL import ImageTk

root = Tk()
root.title("PLACES TO VISIT")
root.geometry("900x1000")


def openfile1():
    with open("/home/nidhi/Documents/Tourist_Guide/marineDrive.txt", "r") as f:
        Message(root, text=f.read()).pack()


def openfile2():
    with open("/home/nidhi/Documents/Tourist_Guide/GateWayOfIndia.txt", "r") as f:
        Message(root, text=f.read()).pack()


def openfile3():
    with open("/home/nidhi/Documents/Tourist_Guide/HajiAliDargah.txt", "r") as f:
        Message(root, text=f.read()).pack()


def openfile4():
    with open("/home/nidhi/Documents/Tourist_Guide/sanjayGandhi.txt", "r") as f:
        Message(root, text=f.read()).pack()


def openfile5():
    with open("/home/nidhi/Documents/Tourist_Guide/kanheriCaves.txt", "r") as f:
        Message(root, text=f.read()).pack()


bg_icon = ImageTk.PhotoImage(file='/home/nidhi/Documents/python mini project/login.jpg')
bg_lbl = Label(root, image=bg_icon).pack()

title = Label(root, text="PLACES TO VISIT IN MUMBAI", font=("times new roman", 40, "bold"),
              bg="light blue", bd=10, relief=GROOVE)
title.place(x=0, y=0, relwidth=1)

p1 = PhotoImage(file='/home/nidhi/Documents/python mini project/marine.png')
p2 = PhotoImage(file='/home/nidhi/Documents/python mini project/gateway.png')
p3 = PhotoImage(file='/home/nidhi/Documents/python mini project/hajiali.png')
p4 = PhotoImage(file='/home/nidhi/Documents/python mini project/sanjaypark.png')
p5 = PhotoImage(file='/home/nidhi/Documents/python mini project/kanheri.png')

btn_1 = tk.Button(root, text="MARINE DRIVE", image=p1, compound=LEFT, command=openfile1,
                  font=("times new roman", 20, "bold"), bg="dark blue", fg="white")
btn_1.place(x=50, y=100)

btn_2 = tk.Button(root, text="GATE WAY OF INDIA", image=p2, compound=LEFT, command=openfile2,
                  font=("times new roman", 20, "bold"), bg="dark blue", fg="white")
btn_2.place(x=50, y=290)
btn_3 = tk.Button(root, text="HAJI ALI DARGAH", image=p3, compound=LEFT, command=openfile3,
                  font=("times new roman", 20, "bold"), bg="dark blue", fg="white")
btn_3.place(x=50, y=460)
btn_4 = tk.Button(root, text="SANJAY GANDHI NATIONAL PARK", image=p4, compound=LEFT, command=openfile4,
                  font=('times new roman', 20, "bold"), bg="dark blue", fg="white")
btn_4.place(x=50, y=640)
btn_5 = tk.Button(root, text="KANHERI CAVES", image=p5, compound=LEFT, command=openfile5,
                  font=("times new roman", 20, "bold"), bg="dark blue", fg="white")
btn_5.place(x=50, y=830)

root.resizable(False, False)
root.mainloop()
