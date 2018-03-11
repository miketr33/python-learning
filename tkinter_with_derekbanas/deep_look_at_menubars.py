from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def quit_app():
    root.quit()

def show_about(event=None):
    messagebox.showwarning(
        "About",
        "Created in 2018 by Mike Tree"
    )

root = Tk()

the_menu = Menu(root)
# ----- The file menu -----
file_menu = Menu(the_menu, tearoff=0)

# The items that will sit inside the file Menu
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")

#   Line on the menu bar
file_menu.add_separator()

file_menu.add_command(label="Quit", command=quit_app)

#   The drop down when you click 'file'
the_menu.add_cascade(label="File", menu=file_menu)

#   ----- Font Menu ------

text_font = StringVar()
text_font.set("Times")

def change_font(event=None):
    print("Font Picked:", text_font.get())

font_menu = Menu(the_menu, tearoff=0)

font_menu.add_radiobutton(label="Times",
                          variable = text_font,
                          command=change_font)
font_menu.add_radiobutton(label="Courier",
                         variable = text_font,
                         command=change_font)
font_menu.add_radiobutton(label="Ariel",
                         variable = text_font,
                         command=change_font)
#   ----- View Menu ------
view_menu = Menu(the_menu, tearoff=0)

line_numbers = IntVar()
line_numbers.set(1) #   True by default

view_menu.add_checkbutton(label="Line Numbers",
                          variable=line_numbers)

view_menu.add_cascade(label="Fonts", menu=font_menu)

the_menu.add_cascade(label="View",menu=view_menu)

#   Show on screen
root.config(menu=the_menu)

root.mainloop()
