class point:
    # constructor to create an object
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # objects
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = point(10, 20)
print(point1.y)

point2 = point(30, 40)
print(point2.y)



class dog:
    # this is a constructor.
    def __init__(self, name, breed):
        self.name = name
        self.breed  = breed

    def bark(self):
        print("woof!!")


# creating an object
dog1 = dog('Tom', 'german shepherd')
#accessing the attributes of the dog1 which is an object
print(dog1.breed)
print(dog1.name)

class person:
    # a constructor to define the attributes
    def __init__(self, name):
        self.name = name


    # method of this class
    def talk(self):
        print(f'Hi, i am {self.name}')


    # creating an object
person1 = person('mary')
person1.talk()

person2 = person('kiash')
person2.talk()
