from tkinter import *
from tkinter.ttk import *
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import joblib

# load the saved logistic Regerssion model
titanic_model = joblib.load('titanic_model' )

# load the saved scaler
scaler = joblib.load('titanic_scaler.pkl')

# constants
WHITE = '#ffffff'


# functions
def predict_survival():
    new_sample = [[Pclass.get(), Age.get(), SibSp.get(), Parch.get(), Fare.get(), male.get(), Q.get(), S.get()]]
    new_sample = scaler.transform(new_sample)
    prediction = titanic_model.predict(new_sample)
    if prediction == 1:
        result = "survived"
        
    else:
        result = "Did not survive"
        
    result_label.config(text=result)
    
    
def reset():
    Pclass.set("")
    Age.set("")
    SibSp.set("")
    Parch.set("")
    Fare.set("")
    male.set("")
    Q.set("")
    S.set("")

# Gui interface using tkinter
window = Tk()
window.title('titanic predicter')
window.geometry('400x400')
window.config(bg = WHITE)
window.resizable(False, False)

#input variables
Pclass = IntVar()
Age = IntVar()
SibSp = IntVar()
Parch = IntVar()
Fare = IntVar()
male = IntVar()
Q = IntVar()
S = IntVar()

#creating input fields
Pclass_entry = Entry(window, textvariable=Pclass)
age_entry = Entry(window, textvariable=Age)
sibsp_entry = Entry(window, textvariable=SibSp)
parch_entry = Entry(window, textvariable=Parch)
fare_entry = Entry(window, textvariable=Fare)
male_entry = Entry(window, textvariable=male)
q_entry = Entry(window, textvariable=Q)
s_entry = Entry(window, textvariable=S)

# create_labels
pclass_label = Label(window, text="Pclass")
age_label = Label(window, text="Age")
sibsp_label = Label(window, text="SibSp")
parch_label = Label(window, text="Parch")
fare_label = Label(window, text="Fare")
male_label = Label(window, text="Male")
q_label = Label(window, text='Q')
s_label = Label(window, text='S')

# positioning the input fields and labels
pclass_label.grid(row=0, column=0, padx=10, pady=10)
age_label.grid(row=1, column=0, padx=10, pady=10)
sibsp_label.grid(row=2, column=0, padx=10, pady=10)
parch_label.grid(row=3, column=0, padx=10, pady=10)
fare_label.grid(row=4, column=0, padx=10, pady=10)
male_label.grid(row=5, column=0, padx=10, pady=10)
q_label.grid(row=6, column=0, padx=10, pady=10)
s_label.grid(row=7, column=0, padx=10, pady=10)

# positioning the input labels
Pclass_entry.grid(row=0, column=1, padx=10, pady=10)
age_entry.grid(row=1, column=1, padx=10, pady=10)
sibsp_entry.grid(row=2, column=1, padx=10, pady=10)
parch_entry.grid(row=3, column=1, padx=10, pady=10)
fare_entry.grid(row=4, column=1, padx=10, pady=10)
male_entry.grid(row=5, column=1, padx=10, pady=10)
q_entry.grid(row=6, column=1, padx=10, pady=10)
s_entry.grid(row=7, column=1, padx=10, pady=10)


# create a predict button
predict_button = Button(window, text='predict_survival', command=predict_survival)
predict_button.grid(row=4, column=2, columnspan=2,padx=30, pady=10)


# creating a reset button
button_reset = Button(window, text='Reset', command=reset)
button_reset.grid(row=5, column=2, columnspan=2,padx=30, pady=10)


# label to display the result
result_label = Label(window, text='waiting for the inputs !!', font=('Comic Sans', 20))
result_label.grid(row=9, column=1, columnspan=2, pady=15)


window.mainloop()