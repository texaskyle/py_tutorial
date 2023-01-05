"""from tkinter import *


def display_mouse_press_cordinates(event):
    print(f"coordinates where mouse clicked: {event.x, event.y}")


window = Tk()

window.bind("<Button-1>", display_mouse_press_cordinates)

window.mainloop()"""

from tkinter import *


def display_mouse_key_pressed(event):
    print(f"coordinates where mouse clicked are: {event.x, event.y}")


window = Tk()

# window.bind("<Button-2>", display_mouse_key_pressed)
# window.bind("<Button-3>", display_mouse_key_pressed)
# window.bind("<ButtonRelease>", display_mouse_key_pressed)
# window.bind("<Enter>", display_mouse_key_pressed)
# window.bind("<Leave>", display_mouse_key_pressed)
window.bind("<Motion>", display_mouse_key_pressed)
window.mainloop()