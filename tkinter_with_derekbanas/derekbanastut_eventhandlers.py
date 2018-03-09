from tkinter import *
from tkinter import ttk

def get_sum(event):
    num1 = int(num1Entry.get())
    num2 = int(num2Entry.get())

    sum = num1 + num2
    #Clears after each entry
    sumEntry.delete(0, "end")

    sumEntry.insert(0, sum)
root = Tk()

#   Note when you take entry as a variable you have to position on a seperate line.
num1Entry = Entry(root)
num1Entry.pack(side=LEFT)

Label(root,text="+").pack(side=LEFT)

num2Entry = Entry(root)
num2Entry.pack(side=LEFT)

equalButton = Button(root, text = "=")

#   Bind left mouse button that when it is clicked the event handler function is called.
equalButton.bind("<Button-1>",get_sum)
equalButton.pack(side=LEFT)

sumEntry = Entry(root)
sumEntry.pack(side=LEFT)

root.mainloop()
