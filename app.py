""" print("texas kyle")
print("O----")
print( " ||||") """

""" price = 100
rating  = 4.9
name = "Evans"
is_employeed = False
print(is_employeed)
print(price)
print(rating)
print(name) """

""" name = "john smith"
age = 20
is_new_patient = False
print(name)
print(age)
print(is_new_patient) """

""" # a program that prompts the user to enter his/her name
first_name = input('what is your  name? ')
print('hi '+first_name) """

""" full_name = input('what is your full name? ')
color = input('what is your favourite color? ')
print(full_name + ' likes ' + color) """

""" birth_year = input('which year were you born in? ')
print(type(birth_year))
age  = 2022 - int(birth_year)
print(type(age))
print('your age is ' + str(age)) """

""" weight = input('what is your weight in pounds? ')
print(type(weight))
to_kilograms = int(weight) / 2
print(type(to_kilograms))
print('kgs = ' + str(to_kilograms)) """

""" course = "python course for begginers"
print(course[0]);
print(course[-3]);
print(course[0:3]); """

""" fname = 'evans'
lname = 'kiarie'
message = fname + ' [' +lname + '] is a coder' 
# formated string
msg  = f'{fname} [{lname}] is a coder'
# print(message)
# print(msg)
print(len(msg)) """


""" course = "python course for begginers"
print(course.upper())
print(course.find('p'))
print(course.replace('course', 'career'))
print('python' in course) """



""" # operators
print(10/3)
print(10 // 3)
print(10**3) #it gives out the power
print(round(10/3)) #performs the rounding off
print(abs(-4.5)) #it always returns a positive value """

"""import math
print(math.lcm(5,10,3))
print(math.gcd(5,10,3))"""

"""age = 21
name = "evans kiarie"
print(f"{name} your age is {age}")
# print(name+ " your age is " + str(age))"""

"""spongebob = patric = kibui = tomas = 30
print(tomas)"""

"""name = "evans kiarie"
# print(len(name))
# print(name.find('ns'))
# print(name.count("a"))
# print(name.replace('e', 'i'))
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name*3)
# print(name.isdigit())"""

"""try:
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    # age = int(age)
    age += 1
    print(f"{name} your age rn is  {age}")
except ValueError:
    print('age can only be of int data type!!')"""


"""# slicing
company = "texas company"
# print(company[0])
# print(company[0:len(company)])
# print(company[0:])
# print(company[:])
# print(company[0 : len(company) : 2])
# print(company[0 : len(company) : 3])"""

# using slice which is kinda diffrent from indexing
website1 = "http://google.com"
website2 = "http://amazom.com"
slice = slice(7, -4)
print(website1[slice])
print(website2[slice])
print(website2[7:-4])