from tkinter import *


def order():
    if x.get() == 0:
        print("you have ordered chapati")
    elif x.get() == 1:
        print("you have ordered githeri")
    elif x.get() == 2:
        print("you are eatinng nyam chom today!!")
    elif x.get() == 3:
        print("are you sure you will taking ice cream")
    else:
        print("huh??")


food = ['chapati', 'githeri', 'nyama', 'ice_cream']
window = Tk()

chapati_image = PhotoImage(file='C:\\Users\\charles\\Pictures\\Screenshot.png')
githeri_image = PhotoImage(file='C:\\Users\\charles\\Pictures\\images.png')
nyama_image = PhotoImage(file='C:\\Users\\charles\\Pictures\\download.png')
ice_cream_image = PhotoImage(file='C:\\Users\\charles\\Pictures\\images.png')

image_list = [chapati_image, githeri_image, nyama_image, ice_cream_image]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],
                              variable=x,
                              value=index,
                              font=('Impact', 30),
                              padx=20,
                              pady=10,
                              image=image_list[index],
                              compound='left',
                              indicatoron=0,
                              width=250,
                              command= order)


    radiobutton.pack(anchor=W)

window.mainloop()