from tkinter import *
from tkinter import messagebox
from tkinter import ttk
def open_msg_box():
    messagebox.showwarning(
        "Event Triggered",   # In the title
        "Button Clicked"    # warning info
    )

root = Tk()

#   Define size (width+height+xoffset+yoffset)
root.geometry("400x400+300+300")

root.resizable(width=False, height=False)

frame = Frame(root)

style = ttk.Style()

style.configure("TButton",
                 foreground="PeachPuff2",
                 font="Times 20 bold italic",
                 padding=20)

# Print all available theme names for your os
print(ttk.Style().theme_names())

#   Find out font on button
print(style.lookup('TButton','font'))
print(style.lookup('TButton','foreground'))
print(style.lookup('TButton','padding'))

ttk.Style().theme_use("alt")

theButton = ttk.Button(frame,
                       text="Important Button",
                       command=open_msg_box)

theButton['state'] = 'disabled'
theButton['state'] = 'normal'

theButton.pack()

frame.pack()

root.mainloop()
