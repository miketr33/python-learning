from tkinter import *   # Import everythng from tkinter lib

class Window(Frame):

    def __init__(self,master=None):
        Frame.__init__(self,master)

        self.master = master

        self.init_window()

    def init_window(self):

        self.master.title("GUI")
        # File up window and adjust dimensions as needed.
        self.pack(fill=BOTH, expand = 1)

        # Create button
        #quitButton = Button(self, text="Quit", command=self.client_exit)
        # Placed in top right
        #quitButton.place(x=0,y=0)



    #def client_exit(self):
        #exit()

root = Tk()
root.geometry("400x300")
app = Window(root)

root.mainloop()
