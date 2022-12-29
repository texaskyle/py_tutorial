""" def greet_user():
    print('hi there!!')
    print('welcome kenya')
print('start')
greet_user()
print('finish') """

""" # parameters
def greet_client(first_name, company):
    print(f'hi {first_name}!!')
    print(f'welcome to {company}')


print('start')
greet_client('evans', 'safaricom')
print('finish')

greet_client('mary', 'ABSA') """

""" #using keyword arguments
def names(first_name, last_name):
    print(f'hi {first_name}')
    print(f'Is {last_name} your last name')

names('evans', 'kiarie') """
    


""" def calc_cost(total, discount, profit):
    print('this are the days transaction')
    print(f'profit is:{profit} discount is: {discount} and total is: {total}')

print('legit business')
calc_cost(profit=50, discount=10, total=200)
print('today was a nice day') """


""" # function that returns a value
def volume(length, width, height):
    return  length * width * height


result = volume(length=5, width=4, height=2)
print(result) """


"""# reusable functions
def emojies_converter(message):
    words = message.split(' ')
    emojies = {
        '(;': chr(128516),
        ';)': chr(128530),
        'wink': chr(128521)
    }
    output= ""
    for word in words:
        output += emojies.get(word, word) + " "
    return output


message = input(">") 
result = emojies_converter(message)
print(result)"""


"""def hello(name, age):
    print("hello !!!" + name)
    print("you are age: " + age)


hello("evans", str(23))"""


"""def multiply(num1, num2):
    return num1 * num2


print(multiply(2, 7))"""


"""# key word arguments
def my_names(first, last, middle):
    print("hello " + first + " " + middle + " " + last)\



my_names(middle="kiarie", last="njoroge", first="evans")"""


"""print(round(abs(float(input("Enter a positive number: ")))))"""

"""# using args
def addition(*args):
    sum = 0
    args = list(args)
    args[0] = 4
    for number in args:
        sum += number
    return sum


print(addition(3, 5, 6, 7, 8))"""


"""# using kwargs
def my_names(**kwargs):
    print('hello ', end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")
my_names(title= 'Mr.', first ="evans", second ="kiarie", last ="kamau")"""


"""pi = 3.1476859
number = 3000333
print(f"The number is {pi:.2f}")
print(f"The number is {number:,}")
print(f"The number is {number:b}")"""

# high orderfunctions
# ----------------------------------------------


def loud(text):
    return text.upper()


"""def quite(text):
    return text.lower()


def hello(func):
    text = func("hello")
    print(text)


hello(loud)
hello(quite)"""

"""# returning a function


def divisor(x):
    def dividend(y):
        return y / x
    return dividend


divide = divisor(2)
print(divide(10))"""


# lambda function
# -------------------------------------------------
"""def double(x):
    return x * 2

print(double(3))"""


double = lambda y: y * 2
print(double(5))
multiply = lambda x, y: x * y
print(multiply(4, 6))
volume = lambda x, y, z: x * y * z
print(volume(3, 4, 5))

names = lambda first_name, last_name: first_name + " " + last_name
print(names("Evans", "Njoroge"))

check_age = lambda age:True if age >= 18 else False
print(check_age(42))



