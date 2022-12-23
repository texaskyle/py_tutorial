import random
# generates a random value between the range of 3
for i in range(3):
    print(random.random())
    print(random.randint(20, 30))

members = ['mary', 'evans', 'kiarie', 'njoroge']
leader = random.choice(members)
print(leader)


# rolling a dice
class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())
