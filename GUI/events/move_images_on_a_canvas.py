from tkinter import *


def move_up(event):
    canvas.move(race_car, 0, -10)


def move_down(event):
    canvas.move(race_car, 0, 10)


def move_left(event):
    canvas.move(race_car, -10, 0)


def move_right(event):
    canvas.move(race_car, 10, 0)




window = Tk()


canvas = Canvas(window, width=500, height=500)
canvas.pack()

photo_image = PhotoImage(file="C:\\Users\\charles\\Pictures\\Audi-Car-Real-PNG.png")
race_car = canvas.create_image(0, 0, image=photo_image, anchor=NW)    # giving a image a new name and specifying the location it will be inserted

window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

window.mainloop()