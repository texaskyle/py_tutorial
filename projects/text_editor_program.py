from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog


def open_file():
    file_path = filedialog.askopenfilename(initialdir='C:\\Users\\charles\\Desktop',  # it returns a file name
                                           title='Opening a File !',
                                           filetypes=(("text files", "*.txt"), ("html files", "*.html"),
                                                      ("python files", "*.py"), ("all file", "*.*")))
    file = open(file_path, 'r')
    print(file.read())


def save_file():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\charles\\Desktop",
                                    title="Saving a File !",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("text files", "*.txt"),
                                        ("html files", "*.html"),
                                        ("all files", ".*")
                                    ])
    file_text = str(text_area.get(1.0, END))
    file.write(file_text)
    file.close()


def new_file():
    pass


# functions for edit menu-----------------------------------------------
def copy_text():
    pass


def cut_file():
    pass


def paste_text():
    pass


# help function------------------------------------
def help():
    pass


window = Tk()
window.geometry('500x500')
window.title("Text editor program")

menu_bar = Menu(window)
window.config(menu=menu_bar) #this code is used for adding menu to the main window

# creating the File menu and add it to the menu bar
file_menu = Menu(menu_bar, tearoff=0, font=("Mv Boli", 15))
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=quit)


edit_menu = Menu(menu_bar, tearoff=0, font=('Mv Boli', 15))
menu_bar.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut_file)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)


help_menu = Menu(menu_bar, tearoff=0, font=("Mv Boli", 15))
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="?Help", command=help)


# entry widget------------------------------------------------------------
text_area = Text(window,
                 font=('Ink Free', 20),
                 fg="purple",
                 bg="light yellow",
                 height=400,
                 width=500)
text_area.pack()

# color chooser button----------------------------------
color_button = Button(window, text='color', width=10, height=2)
color_button.pack()



window.mainloop()