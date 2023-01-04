from tkinter import *
from tkinter import filedialog


def openFile():
    filepath = filedialog.askopenfilename()
    file = open(filepath, 'r')
    print(file.read())


def saveFile():
    file = filedialog.asksaveasfile(filetypes=[
        ("text files", "*.txt"),
        ("all files", ".*")
    ])
    if file is None:
        return
    filetext = str(text_area.get(1.0, END))
    file.write(filetext)
    file.close()
    print("You have saved this file")


def copy_text():
    print("You have copied some text")


def cut_text():
    print("You have cut this text")


def paste_text():
    print("You have pasted this text")


def submit_text():
    file = filedialog.asksaveasfile(filetypes=[
        ("text files", "*.txt"),
        ("all files", ".*")
    ])
    if file is None:
        return
    filetext = str(text_area.get(1.0, END))
    file.write(filetext)
    file.close()


def help():
    with open('C:\\Users\\charles\\Desktop\\help_page.txt') as file:
        print(file.read())



window = Tk()

# photos
saveImage = PhotoImage(file='C:\\Users\\charles\\Pictures\\save.png')

menu_bar = Menu(window)
window.config(menu=menu_bar) #setting the menu of this window to the menubar i have just created

fileMenu = Menu(menu_bar, tearoff=0, font=("Mv Boli", 15))
menu_bar.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='Save', command=saveFile, image=saveImage, compound='left')
fileMenu.add_command(label='Open', command=openFile)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=quit)

editMenu = Menu(menu_bar, tearoff=0,font=("Mv Boli", 15))
menu_bar.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Copy', command=copy_text)
editMenu.add_command(label='Cut', command=cut_text)
editMenu.add_command(label='Paste', command=paste_text)

helpMenu = Menu(menu_bar, tearoff=0, font=("Mv Boli", 15))
menu_bar.add_cascade(label='Help', menu=helpMenu)
helpMenu.add_command(label="?Help", command=help)


# text area
text_area=Text(window,
               font=('Ink Free', 20),
               fg='purple',
               bg='light yellow',
               width=25,
               height=10)
text_area.pack()

button_save = Button(window,
                     text='Submit',
                     command=submit_text)
button_save.pack()


window.mainloop()
