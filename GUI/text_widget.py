from tkinter import *
from tkinter import colorchooser


def submit_text():
    print(text.get('1.0', END)) #1.0 is the index of the first line, the second line will be 2.0


def change_background():
    color = colorchooser.askcolor()
    color_hex = color[1]
    window.config(bg=color_hex)


window = Tk()
text = Text(window,
            bg='light yellow',
            font=('Ink Free', 25),
            fg='purple',
            height=8,
            width=25,
            padx=20,
            pady=20)
text.pack()

button = Button(window,
                text='Submit',
                command=submit_text)
button.pack()

background_button = Button(window,
                           text='Change background',
                           command=change_background)
background_button.pack(side=RIGHT)
window.mainloop()