from tkinter import *
import webbrowser

def netflix():
	webbrowser.open('http://www.netflix.com/')
def google():
	webbrowser.open('http://www.google.com/')
def gmail():
	webbrowser.open('http://www.gmail.com/')
def facebook():
	webbrowser.open('http://www.facebook.com/')
def youtube():
	webbrowser.open('http://www.youtube.com/')

root=Tk()
root.title("Various")

logo1=PhotoImage(file="/home/maverick/Desktop/work/images/netflix1.png")
logo2=PhotoImage(file="/home/maverick/Desktop/work/images/facebook.png")
logo3=PhotoImage(file="/home/maverick/Desktop/work/images/gmail.png")
logo4=PhotoImage(file="/home/maverick/Desktop/work/images/google.png")
logo5=PhotoImage(file="/home/maverick/Desktop/work/images/youtube-logo-hd-8.png")

button1=Button(root,image=logo1,width=200,command=netflix,bd=0,pady=10).grid(row=0,ipady=10)
button2=Button(root,image=logo2,width=200,command=facebook,bd=0,pady=10).grid(row=1,ipady=10)
button3=Button(root,image=logo3,width=200,command=gmail,bd=0,pady=10).grid(row=2,ipady=10)
button4=Button(root,image=logo4,width=200,command=google,bd=0,pady=10).grid(row=3,ipady=10)
button5=Button(root,image=logo5,width=200,command=youtube,bd=0).grid(row=4,ipady=0)

root.mainloop()