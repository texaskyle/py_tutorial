from tkinter import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

photo_image = PhotoImage(file='C:\\Users\\charles\\Pictures\\UFO-PNG-HD-Photo (1).png')
ufo_image = canvas.create_image(0, 0, image=photo_image, anchor=NW) #renaming the image and specifing  the position in the window

while True:
    coordinates = canvas.coords(ufo_image)
    print(coordinates)
    canvas.move(ufo_image, 1, 1)
    window.update()
    time.sleep(0.01)

window.mainloop()