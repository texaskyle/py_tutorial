from tkinter import *


def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y


def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)


window = Tk()

label1 = Label(window, width=10, height=5, bg='red')
label1.place(x=0, y=0)

label2 = Label(window, width=10, height=5, bg='blue')
label2.place(x=100, y=100)

label1.bind("<Button-1>", drag_start)
label1.bind('<B1-Motion>', drag_motion)

label2.bind("<Button-1>", drag_start)
label2.bind("<B1-Motion>", drag_motion)
window.mainloop()


































"""from tkinter import *


def drag_start(event):
    label_a.startX = event.x
    label_a.startY = event.y


def drag_motion(event):
    x = label_a.winfo_x() - label_a.startX + event.x
    y = label_a.winfo_y() - label_a.startY + event.y
    label_a.place(x=x, y=y)


window = Tk()

label_a = Label(window, width=6, height=3, bg='red')
label_a.place(x=0, y=0)

label_a.bind("<Button-1>", drag_start)
label_a.bind("<B1-Motion>", drag_motion)


window.mainloop()"""