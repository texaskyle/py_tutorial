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


 # reusable functions
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
print(result)



