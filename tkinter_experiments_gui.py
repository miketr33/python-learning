from tkinter import *
from tkinter import filedialog

#root_dir = ""

def locate_pathname(event):
    '''
    When user browses for directory
    '''
    rootDirectory = filedialog.askdirectory()
    root_dir = str(rootDirectory)
    results_output(root_dir)

def store_pathname(event):
    '''
    When user enters the pathname
    '''
    pathname = pathnameEntryBox.get()
    root_dir = str(pathname)
    results_output(root_dir)

def results_output(root_dir):
    '''
    Window appears if root dir found
    '''

    ''' CONTINUE FROM HERE TOMORROW - NEED TO CREATE BUTTONS & LINK WITH THE MAIN PROGRAM'''
    if root_dir:
        result_window = Tk()
        result_window.title('Results')
        result_window.geometry("500x500+300+300")

        Label(result_window,text="Results are in for:",anchor=W,justify=LEFT).pack()
        Label(result_window,text=root_dir,wraplength=500,anchor=W,justify=LEFT).pack()


root = Tk()
root.title('Loop Check')
root.geometry("203x138+300+300")

#   Area to browse for dirctory and save to variable.
Label(root,text="Please locate loops folder").grid(row=0,column=1,padx=5,pady=3)
browseButton = Button(root,text = "Browse")
browseButton.bind("<Button-1>",locate_pathname)
browseButton.grid(row=1,column=1)

#   For copying pathname in and saving to variable.
Label(root,text="Or enter loop pathname").grid(row=2,column=1,padx=5)
pathnameEntryBox = Entry(root)
pathnameEntryBox.grid(row=3,column=1,padx=5)
#   When you hit return it does the same as hitting submit.
root_dir = str(pathnameEntryBox.bind("<Return>",store_pathname))
#   Hit 'submit' to check the pathname
submitButton = Button(root,text="Submit")
root_dir = str(submitButton.bind("<Button-1>",store_pathname))
submitButton.grid(row=4,column=1)



root.mainloop()
