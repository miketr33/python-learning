from tkinter import *   # Imports everything
from tkinter import ttk # Several tkinter widgets such as buttons etc

root = Tk() # main window - standard convention to call it 'root'

root.title("First GUI") # Window title

ttk.Button(root, text="Hello TkInter").grid()   # Creates button from ttk lib

root.mainloop() # Keeps root window visable and keeps it running.
