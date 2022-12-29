""" matrix = [
    [1 ,2 ,3],
    [4 ,5 ,6],
    [7 ,8 ,9]
]

matrix[0][1] = 20
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item) """

""" # diffrent functions that can be performed on a list
list = [2, 5, 6, 5, 7, 9]
list.append(20) #inserts at the end of the list
list.insert(0, 33) #ypu can specify where you want the item to be inserted
list.remove(20) #remove an item on the list
# list.clear() #removes all the items on the list
list.pop() #removes the last item on the list
print(list.index(7)) #gives the index where the item is found
print(50 in list) #checks the existence of an item on the list
print(list.count(5)) #it shows how many times a item appears
list.sort() #sorts the items on the list
list.reverse()
list2= list.copy()
print(list2)
list.append(66)

print(list)
 """


"""numbers = [2,3,4,5,5,6,7,7,2]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)"""


"""# unpacking a tuple
coordinates = (1, 2, 3)
x, y, z = coordinates
print(y)"""

"""foods = ["pizzah", "humberger", "chapati", "spaghetti"]
foods[0] = "waruu"
foods.append("beans")
print(foods.index("humberger"))
foods.remove("chapati")
# print(foods[0])
for food in foods:
    print(food)

print("pizzah" in foods)
print("chapati" in foods)
foods.reverse()
print(foods)"""

"""drinks = ["soda", "juice", "tea", "soup"]
dessert = ["cake", "ice cream", "cock tail"]
meat = ["white meat", "red meat"]
alcohol = ["gilberys", "jack daniel", "people", "kenya kane"]

food_list = [drinks, dessert, meat]
food_list.append(alcohol)
print(food_list)
print(food_list[0])
print(food_list[2][1])"""

"""# tuple are very similar to list
student = ("evans", 21, "male")
print(student.count("evans"))
print(student.index("male"))
for student_details in student:
    print(student_details)

if "evans" in student:
    print("Evans is a student!")
else:
    print("may be he is a civilian")
"""

# sorting in list
"""students = ["Evans", "keziah", "lucy", "uhuru", "Ruto"]
students.sort(reverse = True)
for i in students:
    print(i)"""

# sorting in tuple
"""students = ("Evans", "keziah", "lucy", "uhuru", "Ruto")
sorted_students = sorted(students, reverse=True)
for i in sorted_students:
    print(i)"""

# sorting by key
"""students = [("Evans", "C", 21),
            ("uhuru", "F", 60),
            ("Ruto", "E", 46),
            ("keziah", "B", 10),
            ("lucy", "A", 17)]

students.sort()
for i in students:
    print(i)

grade = lambda grades: grades[1]
students.sort(key= grade)
for i in students:
    print(i)

age = lambda ages: ages[2]
students.sort(key= age)
for i in students:
    print(i)"""

# list comprehension
# --------------------------------------------------
# square = []
"""for i in range(1,11):
    square.append(i * i)
print(square)"""

"""square = [i * i for i in range(1, 11)]
print(square)"""

"""grades = [100, 90, 80, 70, 60, 50, 40, 30, 0]
lambda grade: grade >=60
passed_students = list(filter(lambda grade: grade >= 60, grades))
for i in passed_students:
    print(i, end=" ")

passed_students = [i for i in grades if i >= 60]
print(passed_students)"""



