from tkinter import *
window = Tk() #instantiate an instance of a window
window.geometry("420x420") #setting the screen size
window.title("texas company") #renaming the window

icon = PhotoImage(file='C:\\Users\\charles\\Pictures\\Screenshots\\Screenshot (2).png')
window.iconphoto(True, icon)
window.config(background="blue")

# adding a photo to a label
photo = PhotoImage(file='C:\\Users\\charles\\Pictures\\images.png')

label = Label(window,text="Texas",
              font=("Arial", 40, "bold"),
              fg='green', #color of the font
              bg="black", # background color of the label
              relief= RAISED, #style of styling the border box or the label
              bd=10, #adding the thickness of the border
              padx=20,
              pady=10,
              image=photo,
              compound='bottom')
label.pack() #useful so that we can display the label in the window
# label.place(x=0, y=0) #specifiying where we want to display the label in the window

window.mainloop()