from tkinter import *
from balls import *
import time

window = Tk()


WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

background_image = PhotoImage(file="C:\\Users\\charles\\Pictures\\—Pngtree— star space transparency background_5439546.png")
background = canvas.create_image(0, 0, image=background_image)
#  because i am creating multiple balls i need a class
volley_ball = Balls(canvas, 0, 0, 50, 1, 1, "red")
tenis_ball = Balls(canvas, 0, 0, 100, 3, 2, "yellow")
basket_ball = Balls(canvas, 0, 0, 120, 4, 6, "orange")
football = Balls(canvas, 0, 0, 80, 8, 6, "pink")
golf_ball = Balls(canvas, 100, 100, 20, 5, 2, "purple")
ball_1 = Balls(canvas, 0, 0, 40, 2, 9, "light yellow")

while True:
    volley_ball.move()
    tenis_ball.move()
    basket_ball.move()
    football.move()
    golf_ball.move()
    ball_1.move()

    window.update()
    time.sleep(0.01)

window.mainloop()
