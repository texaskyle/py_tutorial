from tkinter import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500
xVelocity = 3
yVelocity = 2

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

background_image = PhotoImage(file="C:\\Users\\charles\\Pictures\\—Pngtree— star space transparency background_5439546.png")
background = canvas.create_image(0, 0, image=background_image)

photo_image = PhotoImage(file='C:\\Users\\charles\\Pictures\\UFO-PNG-HD-Photo (1).png')
ufo_image = canvas.create_image(0, 0, image=photo_image, anchor=NW) #renaming the image and specifing  the position in the window

image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(ufo_image)  #this will give the output as a list
    print(coordinates)
    if coordinates[0] >= WIDTH - image_width or coordinates[0] < 0:
        xVelocity = xVelocity * -1
    if coordinates[1] >= HEIGHT - image_height or coordinates[1] < 0:
        yVelocity = yVelocity * -1
    canvas.move(ufo_image, xVelocity, yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()