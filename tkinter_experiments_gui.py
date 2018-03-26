from tkinter import *
from tkinter import filedialog

class GuiMain(object):
    def __init__(self,root):
        self.root = root
        root.title('Loop Check')
        root.geometry("203x138+300+300")

        #   Area to browse for dirctory and save to variable.
        Label(root,text="Please locate loops folder").grid(row=0,column=1,padx=5,pady=3)
        browseButton = Button(root,text = "Browse")
        browseButton.bind("<Button-1>",self.locate_pathname)
        browseButton.grid(row=1,column=1)

        #   For copying pathname in and saving to variable.
        Label(root,text="Or enter loop pathname").grid(row=2,column=1,padx=5)
        pathnameEntryBox = Entry(root)
        pathnameEntryBox.grid(row=3,column=1,padx=5)
        #   When you hit return it does the same as hitting submit.
        root_dir = str(pathnameEntryBox.bind("<Return>",self.store_pathname))
        #   Hit 'submit' to check the pathname
        submitButton = Button(root,text="Submit")
        submitButton.grid(row=4,column=1)
        root_dir = str(submitButton.bind("<Button-1>",self.store_pathname))

    def locate_pathname(self,event):
        '''
        When user browses for directory
        '''
        rootDirectory = filedialog.askdirectory()
        root_dir = str(rootDirectory)
        if root_dir:
            self.results(root_dir)

    def store_pathname(self,event):
        '''
        When user enters the pathname
        '''
        pathname = pathnameEntryBox.get()
        root_dir = str(pathname)
        if root_dir:
            self.results(root_dir)

    def results(self,root_dir):
        '''
        Window appears if root dir found
        '''
        result_window = Tk()
        result_window.title('Results')
        result_window.geometry("500x500+300+300")

        summaryFrame = Frame(result_window)
        summaryFrame.pack(side=TOP)
        optionsFrame = Frame(result_window)
        optionsFrame.pack(side=TOP)
        Label(summaryFrame,text="Results are in for:",anchor=W,justify=LEFT).pack()
        Label(summaryFrame,text=root_dir,wraplength=500,anchor=W,justify=LEFT).pack()

        Button(optionsFrame,text="Copy to Clipboard").grid(row=0,column=0)
        Button(optionsFrame,text="Save to File").grid(row=0,column=1)
        Button(optionsFrame,text="Rescan").grid(row=0,column=2)

        Button(optionsFrame, text="Start Again", command=result_window.destroy).grid(row=0,column=3)

class menuSystem(GuiMain):
    def __init__(self):
        '''Setup Menus'''
        menuBar = Menu(root)
        self.menuBar = menuBar

        root.config(menu=menuBar)   #   Display the menu
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="Quit", command=root.quit)
        menuBar.add_cascade(label="File", menu=fileMenu)

        helpMenu = Menu(menuBar,tearoff=0)
        helpMenu.add_command(label="Instructions")  # Needs function
        helpMenu.add_command(label="Contact")   # Needs function
        helpMenu.add_command(label="FAQ")   # Needs function
        menuBar.add_cascade(label="Help", menu=helpMenu)

root = Tk()

my_gui = GuiMain(root)
menuSystem()

root.mainloop()
