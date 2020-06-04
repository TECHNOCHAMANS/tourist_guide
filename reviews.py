import sqlite3
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('500x500')
root.title("GIVE REVIEW")

label = Label(root, text="THANK YOU FOR FOR REVIEW", font=("", 20, "bold"), bg="black", fg="white")
label.pack(side=TOP, fill=X)
label = Label(root, text="", font=("", 15, "bold"), bg="black", fg="white")
label.pack(side=BOTTOM, fill=X)


def create():
    conn = sqlite3.connect("/home/nidhi/Documents/Tourist_Guide/database.db")
    c = conn.cursor()
    c.execute(""" CREATE TABLE IF NOT EXISTS reviews(name TEXT ,review TEXT )""")
    conn.commit()
    conn.close()


create()

label = Label(root, text="Enter Review Here", font=("", 15, "bold"))
label.place(x=30, y=150)

review_entry = StringVar()
review_entry = ttk.Entry(root, textvariable=review_entry)
review_entry.place(x=30, y=200)

label = Label(root, text="NAME", font=("", 15, "bold"))
label.place(x=30, y=40)

name_entry = StringVar()
name_entry = ttk.Entry(root, textvariable=name_entry)
name_entry.place(x=30, y=90)


def savedata():
    conn = sqlite3.connect('/home/nidhi/Documents/Tourist_Guide/reviews.db')
    c = conn.cursor()
    c.execute('INSERT INTO reviews(name , review) VALUES (?,?)', (name_entry.get(), review_entry.get()))
    conn.commit()
    print('saved')


btn = ttk.Button(root, text="SAVE REVIEW", command=savedata)
btn.place(x=170, y=400)

root.resizable(False, False)
root.mainloop()
