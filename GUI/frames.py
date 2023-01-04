from tkinter import *

window = Tk()

frame_top = Frame(window, bg='pink', bd=5, relief='sunken')
frame_top.place(x=0, y=0)

Button(frame_top, text='Q', width=6, height=3).pack(side=LEFT)
Button(frame_top, text='W', width=6, height=3).pack(side=LEFT)
Button(frame_top, text='E', width=6, height=3).pack(side=LEFT)
Button(frame_top, text='R', width=6, height=3).pack(side=LEFT)
Button(frame_top, text='T', width=6, height=3).pack(side=LEFT)
Button(frame_top, text='Y', width=6, height=3).pack(side=LEFT)
Button(frame_top, text='U', width=6, height=3).pack(side=LEFT)
Button(frame_top, text='I', width=6, height=3).pack(side=LEFT)
Button(frame_top, text='O', width=6, height=3).pack(side=LEFT)
Button(frame_top, text='P', width=6, height=3).pack(side=LEFT)

frame_middle = Frame(window, bg='pink', bd=5, relief='sunken')
frame_middle.place(x=30, y=70)

Button(frame_middle, text='A', width=6, height=3).pack(side=LEFT)
Button(frame_middle, text='S', width=6, height=3).pack(side=LEFT)
Button(frame_middle, text='D', width=6, height=3).pack(side=LEFT)
Button(frame_middle, text='F', width=6, height=3).pack(side=LEFT)
Button(frame_middle, text='G', width=6, height=3, bd=2, relief="raised").pack(side=LEFT)
Button(frame_middle, text='H', width=6, height=3).pack(side=LEFT)
Button(frame_middle, text='J', width=6, height=3).pack(side=LEFT)
Button(frame_middle, text='K', width=6, height=3).pack(side=LEFT)
Button(frame_middle, text='L', width=6, height=3).pack(side=LEFT)

frame_bottom = Frame(window, bg='pink', bd=5, relief='sunken')
frame_bottom.place(x=60, y=140)

Button(frame_bottom, text='Z', width=6, height=3).pack(side=LEFT)
Button(frame_bottom, text='X', width=6, height=3).pack(side=LEFT)
Button(frame_bottom, text='C', width=6, height=3).pack(side=LEFT)
Button(frame_bottom, text='V', width=6, height=3).pack(side=LEFT)
Button(frame_bottom, text='B', width=6, height=3).pack(side=LEFT)
Button(frame_bottom, text='N', width=6, height=3).pack(side=LEFT)
Button(frame_bottom, text='M', width=6, height=3).pack(side=LEFT)

frame_spacebar = Frame(window, bg='pink', bd=5, relief='sunken')
frame_spacebar.place(x=126, y=210)

Button(frame_spacebar, text=" ", width=30, height=3).pack()

window.mainloop()