from tkinter import *

def display():
    if x.get() == 1 :
        print('i agree')
    else:
        print("i don't agree")


window =Tk()

x = IntVar()
like_photo = PhotoImage(file='C:\\Users\\charles\\Pictures\\download.png')
checkbutton = Checkbutton(window,
                          text='I agree with this!!',
                          variable=x,
                          onvalue=1,
                          offvalue=0,
                          font=('Arial', 20),
                          fg='#00ff00',
                          bg='black',
                          activeforeground='#00ff00',
                          activebackground='black',
                          command=display,
                          padx=20,
                          pady=10,
                          image=like_photo,
                          compound='left'
                          )
checkbutton.pack()

window.mainloop()