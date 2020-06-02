
from tkinter import * 
from PIL import ImageTk
from tkinter import messagebox

class Info_System:
	def __init__(self,root):
		self.root=root
		self.root.title("PLACES TO VISIT")
		self.root.geometry("1000x1500+0+0")
		
		self.bg_icon=ImageTk.PhotoImage(file='login.jpg')   #for jpg photo
		#self.user_icon=PhotoImage(file='user1.png')  #give the full path eg:/home/nidhi/Documents/python mini project/kanheri.png
		self.p1=PhotoImage(file='marine.png')
		self.p2=PhotoImage(file='gateway.png')
		self.p3=PhotoImage(file='hajiali.png')
		self.p4=PhotoImage(file='sanjaypark.png')

		bg_lbl= Label(self.root,image=self.bg_icon).pack()
		title = Label(self.root,text="PLACES TO VISIT IN MUMBAI",font=("times new roman",40,"bold"),bg="light blue",bd=10,relief=GROOVE)
		title.place(x=0,y=0,relwidth=1)

		Info_frame=Frame(self.root,bg="light blue")
		Info_frame.place(x=150,y=100)
		

		btn_1=Button(Info_frame ,text="MARINE DRIVE",image=self.p1,compound=LEFT,font=("times new roman",20,"bold"),bg="dark blue",fg="white").grid(row=1,column=0,pady=10)

		btn_2=Button(Info_frame ,text="GATE WAY OF INDIA",image=self.p2,compound=LEFT,font=("times new roman",20,"bold"),bg="dark blue",fg="white").grid(row=2,column=0,pady=10)
	
		btn_3=Button(Info_frame ,text="HAJI ALI DARGAH", image=self.p3,compound=LEFT,font=("times new roman",20,"bold"),bg="dark blue",fg="white").grid(row=3,column=0,pady=10)

		btn_4=Button(Info_frame ,text="SANJAY GANDHI NATIONAL PARK", image=self.p4,compound=LEFT,font=("times new roman",20,"bold"),bg="dark blue",fg="white").grid(row=4,column=0,pady=10)

 


root=Tk()
obj=Info_System(root)
root.mainloop()

