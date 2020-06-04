import tkinter as tk
from tkinter import *
from PIL import ImageTk
q

root = Tk()
root.geometry("900x900")
root.title('WELCOME')
bg_icon = ImageTk.PhotoImage(file='/home/nidhi/Documents/python mini project/login.jpg')
bg_lbl = Label(root, image=bg_icon).pack()


label = tk.Label(root, text=" WELCOME TO TOURIST GUIDE", font=("", 30, "bold"), bg='black',fg='white')
label.place(x=150, y=50)

label = tk.Label(root, text="")
label.place(x=150, y=70)

p1 = PhotoImage(file='/home/nidhi/Documents/python mini project/1.png')
lb = tk.Label(root,image=p1)
lb.place(x=10,y=170)

p2 = PhotoImage(file='/home/nidhi/Documents/python mini project/places.png')
lb1 = tk.Label(root,image=p2)
lb1.place(x=350,y=170)


btn = tk.Button(root, text="PRESS TO CONTINUE",bg='black',fg='white',)
btn.place(x=600, y=800)




root.mainloop()
