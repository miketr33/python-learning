from tkinter import *
from tkinter import ttk
from tkinter import filedialog

#     Look up tkFileDialog.askdirectory() to open open directories (folders)
#     Read answer here: https://stackoverflow.com/questions/44887576/how-make-drag-and-drop-interface

root = Tk()

root.geometry("400x400+300+300")

Label(root, text = "Options").grid(row = 0,column = 3, sticky = E, padx = 4)

pathname_entry_but = Button(root, text = "Enter Pathname").grid(row = 1, column = 3, sticky = E, padx = 4)
file_picker_but = Button(root, text = "Open File").grid(row = 2, column = 3, sticky = E, padx = 4)

canvas = Canvas(root,width=200,height=150)
canvas.grid(row = 0,column = 0, sticky = W, padx =10)
canvas.create_rectangle(4,10,190,140,fill="Khaki3")
#canvas=Canvas()
#canvas.create_rectangle(10,10,210,210, dash = (4,2))   # Top line

#print(root.filedirectory)
root.mainloop()
