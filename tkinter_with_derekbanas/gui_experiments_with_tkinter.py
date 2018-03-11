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


print(root.filedirectory)
root.mainloop()
