from tkinter import *


def submit():
    user_name = entry.get()
    print("hello " + user_name)
    entry.config(state=DISABLED)



def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get())-1, END)


window = Tk()

entry = Entry(window,
              font=('Arial', 40),
              fg='#00ff00',
              bg='#000000',
              # show="*"
              )
# entry.insert(0, 'texas>')
entry.config(show="#")
entry.pack(side=LEFT)

submit_button = Button(window,
                       text='submit',
                       command=submit
                       )
submit_button.pack(side=RIGHT)

delete_button = Button(window,
                       text="Delete",
                       font=('Arial', 12, 'bold'),
                       fg='red',
                       bg='black',
                       command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,
                          text='backspace',
                          command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()