from tkinter import *
from tkinter import colorchooser


def click():
    color = colorchooser.askcolor()
    color_hex = color[1]
    window.config(bg=color_hex)


window = Tk()
window.geometry('250x300')
button = Button(window,
                text='Click Me', command=click)
button.pack()


window.mainloop()