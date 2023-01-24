from tkinter.ttk import *
from tkinter import *
from time import *
from datetime import datetime
from threading import Thread
from pygame import mixer



bg_color = '#ffffff'
color_1 = '#566FC6'  # blue
color_2 = '#000000'  # black


# functions
def update_clock():
    current_time = strftime("%I:%M:%S:%p")
    time_label.config(text=current_time)
    time_label.after(1000, update_clock)


def sound_alarm():
    mixer.music.load("C:\\Users\\charles\\Desktop\\py_tutorial\\projects\\Alarm_Clock_Project\\sound_music.mp3")
    mixer.music.play()
    selected.set(0)

    # the deactivate button
    deactivate_button = Radiobutton(frame_body, text="Deactivate", font='arial 10 bold', bg=bg_color, fg=color_1, value=2, command=deactivate_alarm)
    deactivate_button.place(x=227, y=95)



def alarm():
    while True:
        control = 1
        print(control)

        alarm_hour = c_hour.get()
        alarm_minute = c_min.get()
        alarm_second = c_sec.get()
        alarm_period = c_period.get()
        alarm_period = str(alarm_period).upper()

        now = datetime.now() # it loads the current datetime
        current_hour = now.strftime("%I")
        current_minute = now.strftime("%M")
        current_second = now.strftime("%S")
        current_period = now.strftime("%p")

        if control == selected.get():
            if alarm_period == current_period:
                if alarm_second == current_second:
                    if alarm_minute == current_minute:
                        if alarm_hour == current_hour:
                            print("time to play the alarm sound")
                            sound_alarm()
                            
        sleep(1)

def activate_alarm():
    thread = Thread(target=alarm)
    thread.start()

# function for deactivating an alarm
def deactivate_alarm():
    print("Deactivate alarm: ", selected.get())
    mixer.music.stop()

# window
window = Tk()
window.title("Alarm clock")
window.geometry('350x170')
window.config(bg=bg_color)

# frame
frame_line = Frame(window, width=400, height=5, bg=color_1)
frame_line.grid(row=0, column=0)

frame_body = Frame(window, width=400, height=290, bg=bg_color)
frame_body.grid(row=1, column=0)

# configuring frame
clock_image = PhotoImage(
    file='C:\\Users\\charles\\Desktop\\py_tutorial\\projects\\Alarm_Clock_Project\\clock.png')
label_image = Label(frame_body, image=clock_image, bg=bg_color)
label_image.place(x=10, y=10)

# displaying the current time
time_text = Label(frame_body, text='Current Time: ', font=('Impact', 15), width=13, height=1, bg=bg_color)
time_text.place(x=10, y=127)

time_label = Label(frame_body, text="", font=("Arial", 20), bg="white", fg="black", width=10, height=1)
time_label.place(x=130, y=123)
# calling the function the current time
update_clock()

name = Label(frame_body, height=1, text='Alarm', font=('Impact', 18), bg=bg_color, fg=color_1)
name.place(x=125, y=10)

hour = Label(frame_body, height=1, text='Hour', font='Ivy 10 bold', bg=bg_color, fg=color_1)
hour.place(x=127, y=40)
c_hour = Combobox(frame_body, font='Ivy 10 bold', width=2)
c_hour['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
c_hour.current(0)
c_hour.place(x=130, y=58)

min = Label(frame_body, height=1, text='Min', font='Ivy 10 bold', bg=bg_color, fg=color_1)
min.place(x=177, y=40)
c_min = Combobox(frame_body, width=2, font='Ivy 10 bold')
c_min['values'] = ("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
c_min.current(0)
c_min.place(x=180, y=58)

sec = Label(frame_body, height=1, text='Sec', font='Ivy 10 bold', bg=bg_color, fg=color_1)
sec.place(x=227, y=40)
c_sec = Combobox(frame_body, width=2, font='Ivy 10 bold')
c_sec['values'] = ("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
c_sec.current(0)
c_sec.place(x=230, y=58)

period = Label(frame_body, height=1, text='Period', font='Ivy 10 bold', bg=bg_color, fg=color_1)
period.place(x=277, y=40)
c_period = Combobox(frame_body, width=4, font='Ivy 10 bold')
c_period['values'] = ('AM', 'PM')
c_period.current(0)
c_period.place(x=280, y=58)

selected = IntVar()

# button for activation
activation_button = Radiobutton(frame_body, text='Activate', font='arial 10 bold',
                                bg=bg_color, fg=color_1, value=1, variable=selected, command=activate_alarm)
activation_button.place(x=130, y=95)

mixer.init()

window.mainloop()

