from tkinter import *

def submit():
    print(f'The current temp is {scale.get()} degrees C')


window = Tk()

hot_image = PhotoImage(file='C:\\Users\\charles\\Pictures\\download.png')
label_hot = Label(image=hot_image)
label_hot.pack()

scale = Scale(window, from_=100,
              to=0,
              length=400,
              orient=VERTICAL,
              tickinterval=10,
              resolution=5,
              font=('Consolas', 20),
              troughcolor='#69EAFF',
              fg='#FF1C00',
              bg='#111111'
              )
scale.pack()

cold_image = PhotoImage(file='C:\\Users\\charles\\Pictures\\images.png')
cold_label = Label(image=cold_image)
cold_label.pack()

button_submit = Button(window,
                       text='submit',
                       command=submit
                       )
button_submit.pack()

window.mainloop()