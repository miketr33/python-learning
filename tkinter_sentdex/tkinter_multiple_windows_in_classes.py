import tkinter as tk
from tkinter import ttk     #   For more stylish GUI buttons etc.

LARGE_FONT = ("Verdana", 12)

'''
Shell for creating windows that can update and move between.
'''

def update():
    '''Need to first clear window then replace with new info'''


#   Define our app class and pass it tk.
class NoiizLoopCheckerApp(tk.Tk):
    #   Initialise method for class
    def __init__(self, *args, **kwargs):
        #   Initialise method for inheritted tk.Tk class (running it).
        tk.Tk.__init__(self, *args, **kwargs)

        #   Container to store a bunch of frames later.
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        #   Configuring row and column to have minimum row height of 0 and column width of 0. With 1 priority.
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #   Predefined dictory to use later (passing into methods)
        self.frames = {}    #  Eventually this will be pack with a bunch of frames.

        #   Loads in all frames within app ready for showing when called.
        for F in (StartPage, ResultPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        #   Calling StartPage to show first but this will change later on.
        self.show_frame(StartPage)

    '''For showing the selected frame'''
    def show_frame(self, cont): #   Cont means 'controller'
        frame = self.frames[cont]   #   Selects frame from 'frames' dictionary
        frame.tkraise() #   Brings the frame to the top for the user to see.

#   First page class, inheriting from tk.Frame
class StartPage(tk.Frame):

    def __init__(self,parent,controller):

        tk.Frame.__init__(self, parent)

        label1 = tk.Label(self, text="This is the start page.")
        label1.pack(pady=10, padx=10)

        button1 = tk.Button(self,text="Next Page",
                            command=lambda: controller.show_frame(ResultPage))
        button1.pack(pady=10, padx=10)

class ResultPage(tk.Frame):

    def __init__(self,parent,controller):

        tk.Frame.__init__(self, parent)

        label1 = tk.Label(self, text="This is the results page.")
        label1.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Start Again",
                            command=lambda: controller.show_frame(StartPage))

        button1.pack(pady=10, padx=10)

        #   Creates label to refresh
        results_of_button = "NO FILE ISSUES"
        self.results_of_button = results_of_button
        label2 = tk.Label(self,text=results_of_button)
        label2.pack(pady=10, padx=10)

        # After button click, label 2 refreshes!
        button2 = tk.Button(self,text="Rescan",command=lambda: self.refresh_results(label2))

        button2.pack(pady=10,padx=10)

    #   Refreshing method
    def refresh_results(self,label_to_update):
        label_to_update[ "text" ]=( "UPDATED" )
        label_to_update.update()

def qf(quickPrint):
    print(quickPrint)



app = NoiizLoopCheckerApp()
app.mainloop()
