""" i =1
while i<5:
    print(i)
    i= i+1
print("Done")
 """


""" #guessing game
secret_no = 7
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = input('Guess a number: ')
    guess_count += 1
    if int(guess) == secret_no:
        print('you won')
        break
else:
    print('you failed') """



""" #car game
user_input = ""
started =False
while True:
    command = input(">" ).lower()
    if command == "start":
        if  started:
            print('car is already started')
        else:
            started = True
            print('car started...ready to go')
    elif command == "stop":
        if not started:
            print('car cannot be stopped multiple times')
        else:
            started  = False
            print('car stopped..ready to break')
    elif command == "help":
        print('start - to start the engine')
        print('stop - to stop the car engine')
        print('quit - to quit the game')
    elif command == "quit":
        break 
    else:
        print('i dont understand the command')  """

""" 
for names in ["evans", "kiarie", "njoroge"]:
    print(names)

#for loop
for items in "python":
    print(items)

for numbers in [1,2,3,4,5,6,7,8,9]:
    print(numbers) """


"""  for numbers in range(10):
     print(numbers)
for numbers in range(0,10,3): #this takes a step 
    print(numbers) """

"""prices = [10, 20, 30, 40, 50]
total = 0
for price in prices:
    total += price
    print(f"total is: {total}")"""


"""# nested loops to generate the cordinates
for x in range(0,4):
    for y in range(0,3):
        print(f"{x}, {y}")"""



"""# example
numbers = [5, 2, 5, 2, 2]
for number in numbers:
    print('x' * number)

items = [5,2,5,2,2]
for x_count in items:
    output = ""
    for x_count in range(x_count):
        output += 'x'
    print(output)
"""
"""names = ['john', 'mary', 'kamau', 'lucy', 'evans']
print(names[4])
print(names[1:4])
names[0] = 'texas'
print(names)
print(names[0:2])"""

"""# a program to find the largest number
numbers = [3,5,8,9,2,4]
max = numbers[0]
for number in numbers:
    if number > max : 
        max = number
print(max)"""


"""# while loop
name = ""
while len(name) == 0:
    name = input("Enter your name: ")

print(f"your name is: {name}")"""

"""# for loop
# for i in range(9, 50+1, 2):
for i in range(10, 15):
    print(i+1)"""


"""name ="evans"
for i in name:
    print(i)"""


"""# a program for count down
import time
for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("happy new year!!" + chr(128516))"""

"""# nested loops
rows = int(input("Enter the number of rows "))
columns = int(input("Enter the number of columns "))
symbol = input("Enter the symbol to use ")

for i in range(rows):
    for j in range(columns):
        # print(symbol, end="")
        print(chr(128516), end="")
    print()"""

"""# loop control statement
while True:
    name = input("Enter your name: ")
    if name != "":
        # break is used to terminate the loop entirely
        break"""

"""phone_number = "123-456-789-0"
for i in phone_number:
    if i == "-":
        # continue skips to the next iteration of the loop
        continue
    print(i, end="")"""

for i in range(1, 10):
    if i == 5:
        # pass does nothing and acts a s the placeholder
        pass
    else:
        print(i)








