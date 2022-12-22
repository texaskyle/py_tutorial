
# error handling
try: #this is the block to be tested for errors
    age = int(input("Age: "))
    retirement_benefits = 20000
    income = retirement_benefits / age
    print(age)
except ZeroDivisionError:
    print("Age can never be zero!!")
except ValueError:
    print("Invalid value")


try:
    a = int(input("a: "))
    b = input("b: ")
    c = a+b
    print(c)
except TypeError:
    print('cannot add a string to an int')
except ValueError:
    print("only interger values accepted!")
except ZeroDivisionError:
    print('cannot divide by zero')
