import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *


def change_color():
    color = colorchooser.askcolor()
    text_area.config(fg=color[1])


def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))


def new_file():
    window.title("Untitled")
    text_area.delete(1.0, END)


def open_file():
    file_path = filedialog.askopenfilename(defaultextension='.txt', filetypes=[
        ("text documents", ".txt"),
        ("all, files", "*.*"),
        ("html", ".html")
    ])
    try:
        window.title(os.path.basename(file_path))
        text_area.delete(1.0, END)
        file = open(file_path, 'r')
        text_area.insert(1.0, file.read())

    except UnicodeDecodeError:
        showerror(title='Error', message='Error in opening file!!')

    except EXCEPTION:
        showerror(title='Error', message='could not open the file')

    finally:
        file.close()


def save_file():
    file = asksaveasfilename(initialfile='Untitled.txt',
                             defaultextension='.txt',
                             filetypes=[
                                 ("text document", ".txt"),
                                 ("html file", ".html")
                             ])
    if file is None:
        return
    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")
            file.write(text_area.get(1.0, END))

        except EXCEPTION:
            showerror(title="Error", message="You experienced an error while saving the file !")

        finally:
            file.close()


def cut():
    text_area.event_generate("<<Cut>>")


def copy():
    text_area.event_generate("<<Copy>>")


def paste():
    text_area.event_generate("<<Paste>>")


def about():
    showinfo(title='About this program', message='This is a program written by Texas Kyle')


def quit():
    window.destroy()


window = Tk()
window.title("Text Editor Program")

file = None

window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

# this code will put the window in the center
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

font_name = StringVar(window)
font_name.set("Arial")

font_size = StringVar()
font_size.set("25")

text_area = Text(window, font=(font_name.get(), font_size.get()))
scrollbar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)
scrollbar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scrollbar.set)

frame = Frame(window)
frame.grid()

color_button = Button(frame, text='Color', command=change_color)
color_button.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)


# creating a menu bar--------------------------------------------------------
menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=quit)


edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Copy', command=copy)
edit_menu.add_command(label='Cut', command=cut)
edit_menu.add_command(label='paste', command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About', command=about)







window.mainloop()


