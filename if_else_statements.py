""" is_hot = False
is_cold = False

if is_hot:
    print('it is a hot day')
    print('drink more water')
elif is_cold:
    print('it a cold day')
    print('wear warm clothes')
else:
    print('it is a lovely day')
print('enjoy your day') """
    

""" price = 1000000
good_credit = False
if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"down payment: ${down_payment}")     """


""" has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("is eligible for loan")
else:
    print('not elibile for loan') """


""" has_high_income = True
has_good_credit = True
criminal_record = True

if has_high_income and not criminal_record:
    
    print("is eligible for loan")
else:
    print('not elibile for loan') """

""" temp = 5

if temp>30:
    print('it is a hot day')
elif temp<10:
    print("it's a cold day")
else:
    print('it is neither hot nor cold') """


""" name = "evans"
if len(name)<3:
    print("name must be at least 3characters!!")
elif len(name)>50:
    print("name can be a max of 50 characters")
else:
    print("name looks good!") """


""" #example
weight = input("Enter your weight ")
kg_or_pounds = input("(L)bs or (K)g: ")

if kg_or_pounds.lower() == "k":
   weight_in_kg = int(weight) * 0.45
   print('weight in pounds is: '+ str(weight_in_kg))
elif kg_or_pounds.lower() == "l":
    weight_in_pounds = int(weight) // 0.45
    print('weight in kg is: '+str(weight_in_pounds))
else:
    print('invalid character') """

try:
    age = int(input("What is your age: "))
    if 18 <= age <= 30:
        print("your are in the youth stage")
    elif 30 < age < 100:
        print("you are an adult")
    elif 18 > age:
        print("you are a child")
    elif age >= 100:
        print("you are a century years old")
    else:
        print("you have entered an incorrect age")
except ValueError:
    print('Age can only be of int type!!')




