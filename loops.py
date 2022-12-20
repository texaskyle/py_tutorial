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

prices = [10, 20, 30, 40, 50]
total = 0
for price in prices:
    total += price
    print(f"total is: {total}")


# nested loops to generate the cordinates
for x in range(0,4):
    for y in range(0,3):
        print(f"{x}, {y}")



# example
numbers = [5, 2, 5, 2, 2]
for number in numbers:
    print('x' * number)

items = [5,2,5,2,2]
for x_count in items:
    output = ""
    for x_count in range(x_count):
        output += 'x'
    print(output)

names = ['john', 'mary', 'kamau', 'lucy', 'evans']
print(names[4])
print(names[1:4])
names[0] = 'texas'
print(names)
print(names[0:2])

# a program to find the largest number
numbers = [3,5,8,9,2,4]
max = numbers[0]
for number in numbers:
    if number > max : 
        max = number
print(max)




