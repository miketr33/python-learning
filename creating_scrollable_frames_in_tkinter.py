'''
Adapted from:
https://stackoverflow.com/questions/17657212/how-to-code-the-tkinter-scrolledtext-module

More research needed on how this works
'''

from tkinter import *
import tkinter.scrolledtext as tkst

win = Tk()
resultsFrame = Frame(win,bg = '#808000')
resultsFrame.pack(fill='both',expand='yes')
editArea = tkst.ScrolledText(
    master = resultsFrame,
    wrap   = WORD,
    width  = 20,
    height = 10
)
# Don't use widget.place(), use pack or grid instead, since
# They behave better on scaling the window -- and you don't
# have to calculate it manually!
editArea.pack(padx=10, pady=10, fill=BOTH, expand=True)
# Adding some text, to see if scroll is working as we expect it
editArea.insert(INSERT,
"""\
RESULTS FROM OUTPUT: Integer posuere erat a ante venenatis dapibus.
Posuere velit aliquet.
Aenean eu leo quam. Pellentesque ornare sem.
Lacinia quam venenatis vestibulum.
Nulla vitae elit libero, a pharetra augue.
Cum sociis natoque penatibus et magnis dis.
Parturient montes, nascetur ridiculus mus.
""")
win.mainloop()
