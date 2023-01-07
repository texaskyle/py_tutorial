from tkinter import *
from time import *


def update_clock():
    current_time = strftime("%I:%M:%S %p")
    time_label.config(text=current_time)
    time_label.after(1000, update_clock)

    current_day = strftime("%A")
    day_label.config(text=current_day)
    day_label.after(86400000, update_clock)

    current_date = strftime("%d/%m/%Y")
    date_label.config(text=current_date)
    date_label.after(86400000, update_clock)



window = Tk()

time_label = Label(window, font=('Arial', 50), fg="#00ff00", bg="black")
time_label.pack()

day_label = Label(window, font=("Ink Free", 30))
day_label.pack()

date_label = Label(window, font=("Ink Free", 20))
date_label.pack()

update_clock()

window.mainloop()