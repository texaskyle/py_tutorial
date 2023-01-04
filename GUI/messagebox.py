from tkinter import *
from tkinter import messagebox


def click():
    #messagebox.showinfo(title='This is an info message box', message='You are a programmer:)')

    """while TRUE:
       # messagebox.showwarning(title='WARNING!', message='You have a VIRUS!!!')"""

    # messagebox.showerror(title='ERROR', message='You experienced an error!!')

    """if messagebox.askokcancel(title='Ask ok cancel', message='Do you want to do the thing!'):
        print('You did the thing!')
    else:
        print('You canceled the thing')"""

    """if messagebox.askretrycancel(title='Ask retry cancel', message='Do you want to retry copy!'):
        print('You have retried the copy!')
    else:
        print('You have canceled the copy!')"""

    """if messagebox.askyesno(title='Ask yes no', message='Do you like coding!'):
        print('You like to code Evans!')
    else:
        print('Why dont you like to code?')"""

    """answer = messagebox.askquestion(title='ask question', message='Do you like to party?')
    if answer == 'yes':
        print('you are addicted in partying bro!')
    else:
        print('You rarely go to parties(:')"""

    answer = messagebox.askyesnocancel(title='ask yes no cancel', message='Do you like to watch tiktok?')
    if answer:
        print("yes i do like tiktok")
    elif (answer == False):
        print('Then why are you always in toktok watching videos!')
    elif answer == None:
        print('You dodged to reply')


window = Tk()

button = Button(window,
                text='Click me',
                command=click)
button.pack()

window.mainloop()