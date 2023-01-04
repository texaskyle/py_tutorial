from tkinter import *
from tkinter import filedialog


def open_file():
    file_path = filedialog.askopenfilename(initialdir="C:\\Users\\charles\\Desktop",
                                           title='Open file okey!!',
                                           filetypes=(("text files", "*.txt"), ("all files", "*.*"))) #returns a file path
    file = open(file_path, 'r')
    print(file.read())


window=Tk()
button = Button(window,
                text='Open',
                command=open_file)
button.pack()
window.mainloop()