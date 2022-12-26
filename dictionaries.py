""" customer = {
    "name" : "Evans kiarie",
    "age" : 21,
    "is_verified": True
}

# print(customer["name"])
print(customer.get("birthDate", "14 feb 2001")) #here you can provide the default value if the key is not specified """


""" # example
phone = input("phone > ")

digits_mapping = {
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '6' : 'six'
}

output = ''
for numbers in phone:
    output += digits_mapping.get(numbers, "!") + " "
print(output) """

"""# dictionaries of capital
capital_city = {"kenya": "nairobi",
                "japan": "toyko",
                "china": "beijing",
                "russia": "moscow"
                }
capital_city.update({"germany": "berlin"})
capital_city.pop("russia")
# capital_city.clear()

# print(capital_city["kenya"])
# print(capital_city.get("germany", "germany"))
# print(capital_city.keys()) #keys() prints only the keys
# print(capital_city.values()) # values() prints only the values
# print(capital_city.items()) #items() prints the entire dictionary

for key, value in capital_city.items():
    print(key, value)"""


      
