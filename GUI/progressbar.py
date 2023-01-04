from tkinter import *
from tkinter.ttk import *
import time


def start():
    download = 0
    GB = 100
    speed = 1
    while download < GB:
        time.sleep(0.05)
        bar['value'] += 10
        download += speed
        progress.set(str(int(download/GB*100)) + "%")
        evaluating_task.set(str(download) + "/" + str(GB) + " GB completed")
        window.update_idletasks()


window = Tk()
progress = StringVar()
evaluating_task = StringVar()


bar = Progressbar(orient=HORIZONTAL, length=300)
bar.pack()

Label(window, textvariable=progress).pack()
Label(window, textvariable=evaluating_task).pack()

Button(window, text='Download', command=start).pack()

window.mainloop()