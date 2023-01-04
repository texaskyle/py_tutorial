from tkinter import *
from tkinter import filedialog


def save_file():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\charles\\Desktop",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("text files", ".txt"),
                                        ("HTML files", ".html"),
                                        ("python files", ".py"),
                                        ("all files", ".*")
                                    ])
    if file is None:
        return
    filetext = str(text.get(1.0, END))
    file.write(filetext)
    file.close()

window=Tk()

text= Text(window,
           font=('Ink Free', 20),
           bg='light yellow',
           fg='purple',
           width=25,
           height=8,
           padx=20,
           pady=20)
text.pack()


button=Button(window,
              text='Save',
              command=save_file)

button.pack()
window.mainloop()