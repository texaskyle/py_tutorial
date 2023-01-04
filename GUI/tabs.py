from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window) #widget that manages a collection of widges or diplays

tab1 = Frame(notebook) #creates a new frame for tab 1
tab2 = Frame(notebook) #creates new frame for tab 2

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack(expand=True, fill='both') # expand = expand to fill any empty space
                                        # fill = fill spaces x and y

Label(tab1, text="This is the first tab", width=50, height=25).pack()
Label(tab2, text='I am Evans and i love coding', width=60, height=30).pack()


window.mainloop()