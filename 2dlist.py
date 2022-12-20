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


numbers = [2,3,4,5,5,6,7,7,2]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)


# unpacking a tuple
coordinates = (1, 2, 3)
x, y, z = coordinates
print(y)