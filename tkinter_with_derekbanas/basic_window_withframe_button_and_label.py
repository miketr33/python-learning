from tkinter import *   # Import all from tkinter lib
from tkinter import ttk

root = Tk()

# A widget that surrounds other widgets.
my_frame = Frame(root)

#   tkinter variable to change text of a label component
labelText = StringVar()

#   creating a label (variable can be called whatever you want)
my_label = Label(my_frame, textvariable = labelText)
#   Create a button with text in
my_button = Button(my_frame, text = "Click Me")

#   Set the label text variable.
labelText.set("I am a label")

#   Positions widgets inside Window using pack() function
my_label.pack()
my_button.pack()
my_frame.pack()

root.mainloop()
