from tkinter import *
import random


GAME_WIDTH = 700
GAME_HEIGHT = 700
SNAKE_COLOR = "#00ff00"
BODY_PARTS = 3
SPACE_SIZE = 50
SPEED = 100
BACKGROUND_COLOR = "#000000"
FOOD_COLOR = "#FF0000"


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food:
    def __init__(self):
        x = random.randint(0, GAME_WIDTH/SPACE_SIZE-1) * SPACE_SIZE
        y = random.randint(0, GAME_HEIGHT/SPACE_SIZE-1) * SPACE_SIZE

        self.coordinates = [x, y]
        canvas.create_oval(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        #     updating the score
        global score

        score += 1

        label.config(text=f"Score: {score}")

        canvas.delete("food")

        #     creating a new food object
        food = Food()

    else:
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collision(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):
    global direction

    if direction == "left":
        if direction != "right":
            direction = new_direction

    if direction == "right":
        if direction != "left":
            direction = new_direction

    if direction == "up":
        if direction != "down":
            direction = new_direction

    if direction == "down":
        if direction != "up":
            direction = new_direction


def check_collision(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x > GAME_WIDTH:
        print("Game over")
        return True

    elif y < 0 or y > GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=("consolas", 70), text="Game Over",fill="#FF0000", tag="game over")


window = Tk()
window.title("Snake Game")
window.resizable(False, False)


# label to store the score
score = 0
label = Label(text=f"score: {score}", font=("impact", 20))
label.pack(side="top")

# initial direction
direction = "down"

canvas = Canvas(window, width=GAME_WIDTH, height=GAME_HEIGHT, bg=BACKGROUND_COLOR)
canvas.pack()

window.update()

# Centering a window-----------------------------------------------------------------
window_width = GAME_WIDTH
window_height = GAME_HEIGHT
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_width/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))

snake = Snake()
food = Food()
next_turn(snake, food)

"""x = random.randint(0, window_width)
y = random.randint(0, window_height)
radius = SPACE_SIZE
color = FOOD_COLOR
if y+radius > window_height and x+radius > window_width:
    y -= SPACE_SIZE
    x -= SPACE_SIZE
if y-radius < 50 and x-radius < 50:
    y += SPACE_SIZE
    x += SPACE_SIZE

print(x)
print(y)
food = Food(canvas, x, y, radius, color)"""

window.mainloop()