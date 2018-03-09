from tkinter import *
from tkinter import ttk

root = Tk()

#   Surrounds our widgets
frame = Frame(root)

Label(frame,text="A Bunch of Buttons").pack()

#   Create button and place on different sides and fills
Button(frame,text = "B1").pack(side = LEFT, fill = Y)
Button(frame,text = "B2").pack(side = TOP, fill = X)
Button(frame,text = "B3").pack(side = RIGHT, fill = X)
Button(frame,text = "B4").pack(side = LEFT, fill = Y)

frame.pack()
root.mainloop()
