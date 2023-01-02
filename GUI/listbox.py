from tkinter import *


def order():
    # print(f' You have ordered {listbox.get(listbox.curselection())}')
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print("You have ordered:")
    for index in food:
        print(index)


def add_item():
    listbox.insert(listbox.size(), entry_box.get())
    listbox.config(height=listbox.size())


def delete_item():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())


window = Tk()

listbox = Listbox(window,
                  bg='#f7ffde',
                  font=('Constantia', 30),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

# inserting items in a list box
listbox.insert(1, "pizzah")
listbox.insert(2, 'chapati')
listbox.insert(3, 'salad')
listbox.insert(4, 'cabbage')
listbox.insert(5, 'nyama')

listbox.config(height=listbox.size())

# entry box for inserting items in a listbox
entry_box = Entry(window)
entry_box.pack()

add_button = Button(window,
                    text='Add',
                    command=add_item
                    )
add_button.pack()
delete_button = Button(window,
                       text='Delete',
                       command=delete_item
                       )
delete_button.pack()


submit_button = Button(window,
                       text='submit',
                       command=order)
submit_button.pack()

window.mainloop()