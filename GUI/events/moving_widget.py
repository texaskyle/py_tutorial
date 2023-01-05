from tkinter import *


def move_up(event):
    label1.place(x=label1.winfo_x(), y=label1.winfo_y()-10)


def move_down(event):
    pass


def move_left(event):
    pass


def move_right(event):
    pass


window = Tk()

car_image = PhotoImage(file='C:\\Users\\charles\\Pictures\\Audi-Car-Real-PNG.png')

label1 = Label(window, image=car_image)
label1.place(x=0, y=0)

label1.bind("<w>", move_up)
label1.bind("<s>", move_down)
label1.bind("<a>", move_left)
label1.bind("<d>", move_right)

window.geometry('500x500')

window.mainloop()