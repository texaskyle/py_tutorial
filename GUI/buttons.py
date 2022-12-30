from tkinter import *

count = 0


def click():
    global count
    count += 1
    print(f"you have clicked this button {count} times")


window = Tk()
like_icon = PhotoImage(file='C:\\Users\\charles\\Pictures\\download.png')
button = Button(window,
                text='click Me',
                command=click,
                font=('Comic Sans', 30),
                fg='#00ff00',
                bg='#000000',
                activebackground='black',
                activeforeground='green',
                image=like_icon,
                compound='bottom'
                )
button.pack()

window.mainloop()