"""from tkinter import *


def do_something(event):
    print(f"You pressed the key: {event.keysym} ")


window = Tk()

# window.bind(event, function)
# window.bind("<Return>", do_something)
window.bind("<Key>", do_something)
window.mainloop()"""

from tkinter import *


def display_key_pressed(event):
    label.config(text=event.keysym)


window = Tk()

window.bind("<Key>", display_key_pressed)

label = Label(window, font=("Arial", 100))
label.pack()

window.mainloop()