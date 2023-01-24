from tkinter.ttk import *
from tkinter import *
from time import *


from pygame import mixer

def sound_alarm():
    mixer.music.load(
        "C:\\Users\\charles\\Desktop\\py_tutorial\\projects\\Alarm_Clock_Project\\alarm_sound.mp3")
    mixer.music.play()

mixer.init()

def alarm():
    current_time = strftime("%I %M %S %p")
    time_label.config(text=current_time)

window = Tk()
window.title("")
window.geometry("350x150")

# sound_alarm()
time_label = Label(window, text="", font=("Impact", 20), bg="black", fg="green")
time_label.pack()
alarm()

window.mainloop()
