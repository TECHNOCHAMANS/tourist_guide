from tkinter import *
import webbrowser
root = Tk()
new=1
def openfile1():
	with open("marineDrive.txt", "r") as f:
		Message(root,text=f.read()).pack()
	#Button(root,text="For More Information",command=webbrowser.open("https://en.wikipedia.org/",new=new)).pack()
def openfile2():
	with open("GateWayOfIndia.txt", "r") as f:
		Message(root,text=f.read()).pack()
	#Button(root,text="For More Information",command=webbrowser.open("https://en.wikipedia.org/wiki/Gateway_of_India",new=new)).pack()
def openfile3():
	with open("HajiAliDargah.txt", "r") as f:
		Message(root,text=f.read()).pack()
	#Button(root,text="For More Information",command=webbrowser.open("https://en.wikipedia.org/wiki/Haji_Ali_Dargah",new=new)).pack()
def openfile4():
	with open("sanjayGandhi.txt", "r") as f:
		Message(root,text=f.read()).pack()
	#Button(root,text="For More Information",command=webbrowser.open("https://en.wikipedia.org/wiki/Sanjay_Gandhi_National_Park",new=new)).pack()
Btn1 = Button(root, text = "Marine Drive",command=openfile1,anchor='center',width=20,bg="pink")
Btn1.pack(side="left")
Btn2 = Button(root, text = "Gate Way of India",command=openfile2,anchor='center',width=20,bg="light blue")
Btn2.pack(side="left")
Btn3 = Button(root, text = "Haji Ali Dargah",command=openfile3,anchor='center',width=20,bg="light green")
Btn3.pack(side="left")
Btn4 = Button(root, text = "Sanjay Gandhi National Park",command=openfile4,anchor='center',width=20,bg="light yellow")
Btn4.pack(side="left")
root.mainloop()
