from tkinter import *


def create_window():
    # new_window = Toplevel()
    new_window = Tk()
    Button(new_window, text='submit').pack()
    new_window.geometry('200x100')
    old_window.destroy()


old_window = Tk()

Button(old_window, text="Create a new window", command=create_window).pack()
old_window.geometry('250x250')
old_window.mainloop()