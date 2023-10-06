import tkinter as tk
from tkinter import *
root = Tk()

#TITLE
root.title("TWITTER SENTIMENT ANALYSIS")
root.iconbitmap('C:/Users/darre/Downloads/twitter_icon.ico')
root.geometry('500x500')
label1=Label(root, text="Enter keyword or hashtag:").pack()

#KEYWORD
k = Entry(root)
k.pack()
button1 = Button(root, text="SUBMIT", bg="green")
button1.pack()
k.get()

#SLIDER
frame1 = LabelFrame(root, padx=5, pady=5)
frame1.pack(padx=10, pady=10)
label2=Label(frame1, text="Select number of Tweets:").pack()
horizontal = Scale(frame1, from_=0, to=500, sliderlength=15, resolution=10, orient=HORIZONTAL).pack() 
button2 = Button(frame1, text="SUBMIT", bg="green")
button2.pack()

#DROPDOWN
options = [
"recent", 
"andi", 
"mandi",
"shandi"
]
frame2 = LabelFrame(root, padx=5, pady=5)
frame2.pack(padx=10, pady=10)
label2=Label(frame2, text="Select date:").pack()
date = IntVar()
date.set(options[0])
drop = OptionMenu(frame2, date, *options)
drop.pack()
button3 = Button(frame2, text="SUBMIT", bg="green")
button3.pack()

root.mainloop()

