""" customer = {
    "name" : "Evans kiarie",
    "age" : 21,
    "is_verified": True
}

# print(customer["name"])
print(customer.get("birthDate", "14 feb 2001")) #here you can provide the default value if the key is not specified """


# example
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
print(output)

      
