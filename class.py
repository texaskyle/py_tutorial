"""class point:
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
print(point2.y)"""



"""class dog:
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
print(dog1.name)"""

"""class person:
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
person2.talk()"""


"""class Car:

    wheels = 4

    def __init__(self, model, color, make, year):
        self.model = model
        self.color = color
        self.make = make
        self.year = year

    def drive(self):
        print(f"The {self.model} already started and it is driving")

    def stop(self):
        print(f"The {self.make} been stopped!!")


car_1 = Car("CX5", "Yellow", "Germany machine", 2022)
print(car_1.make)
print(car_1.year)
print(car_1.color)
print(car_1.model)
print("wheels: " + str(car_1.wheels))
car_1.drive()
car_1.stop()

print("--------------------")

car_2 = Car("A-class", "blue", "Mercedez-Benz", 2022)
print(car_2.model)
print(car_2.make)
print(car_2.color)
print(car_2.year)
print()
car_2.drive()
car_2.stop()"""


"""# inheritance
# ------------------------------------------------------------------------------------
class Animals:
    alive = True
    def eating(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping!")

class Rabbits(Animals):
    def run(self):
        print("This rabbits is running!!")

class Fish(Animals):
    def swim(self):
        print("This fish is swimming")

class Chicken(Animals):
    def products(self, product):
        print(f"This bird is kept for {product}")


rabbit = Rabbits()
print(rabbit.alive)
rabbit.run()
print("--------------------")

fish = Fish()
print(fish.sleep())
fish.swim()
print("--------------------")

broiler = Chicken()
broiler.eating()
broiler.products("meat")

layers = Chicken()
layers.eating()
layers.products("eggs")"""

"""# ---------------------------------------------------
# multi-level inheritance
class Organism:
    alive = True
class Animals(Organism):
    def eat(self):
        print("This animal is eating")
class Dogs(Animals):
    def bark(self):
        print("This dog is barking!")

dog = Dogs()
print(dog.alive)
dog.bark()
dog.eat()"""


"""# multiple inheritance
# --------------------------------------------
class Prey:
    def flee(self):
        print("This animal flees")
class Predator:
    def hunt(self):
        print("This animal is hunting")


class Rabbit(Prey):
# method overriding
    def flee(self):
        print("A rabbit is being hunted by a lion!!")


class Lion(Predator):
    pass
class Fish(Prey, Predator):
    pass


rabbit = Rabbit()
lion = Lion()
fish = Fish()

rabbit.flee()
lion.hunt()
fish.hunt()
fish.flee()"""


"""# method chaining
# ----------------------------------------------------------
class Car:
    def start(self):
        print("The car has been turned on")
        return self

    def drive(self):
        print("The car is driving")
        return self

    def breaking(self):
        print("The car is breaking")
        return self

    def stop(self):
        print("The car has been stopped!!")
        return self


car_1 = Car()
car_1.start()\
    .drive()\
    .breaking()\
    .stop()"""


# abstract methods
# ----------------------------------------------
"""from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        print("This vehicle is moving")
    @abstractmethod
    def breaking(self):
        print("This vehicle is breaking")
class Motorcycle(Vehicle):
    def go(self):
        print("This motorcycle is moving")

    def breaking(self):
        print("This motorcycle is breaking")
class Car(Vehicle):
    def go(self):
        print("This car is driving")

    def breaking(self):
        print("This car is breaking in a corner!")


motorcycle = Motorcycle()
motorcycle.go()
motorcycle.breaking()
print("--------")

car = Car()
car.go()
car.breaking()"""

# passing objects as arguments
# ------------------------------------------------------
"""class Car:
    color = None


def change_color(car, color):
    car.color = color


car_1 = Car()
car_2 = Car()
car_3 = Car()

change_color(car_1, "red")
change_color(car_2, "white")
change_color(car_3, "yellow")

print(car_1.color)
print(car_2.color)
print(car_3.color)"""

# duck typing
# --------------------------------------------
class Duck:
    def walk(self):
        print("This duck is walking")
    def talk(self):
        print("This duck is qwuacking")

class Chicken:
    def walk(self):
        print("This chicken is walking")
    def talk(self):
        print("This chicking is clucking")


class Person:
    def catch(self, duck):
        duck.walk()
        duck.talk()


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)


