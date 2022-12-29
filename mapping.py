"""store = [("shirts", 5.00),
         ("shorts", 2.00),
         ("jackets", 20.00),
         ("boots", 50.00)]

price_to_kshs = lambda data: (data[0], str(data[1]*100) + " kshs")

store_kenyan = list(map(price_to_kshs, store))
for i in store_kenyan:
    print(i)"""


"""friends = [("sonnie", 23),
           ("kyle", 21),
           ("kakem", 22),
           ("keziah", 9),
           ("ndugu", 16)]

drinking_age = lambda data: data[1] >= 18

drinking_buddies = list(filter(drinking_age, friends))
for i in drinking_buddies:
    print(i)"""

import functools
letters = ["M", "A", "N", "C", "H", "E", "S", "T", "E", "R"]
lambda x, y: x + y
word = functools.reduce(lambda x, y: x + y, letters)
print(word)

