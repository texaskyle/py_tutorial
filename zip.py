username = ["kyle", "evans", "njoroge"]
password = ["p@ssword", "1234", "yours345"]

users = dict(zip(username, password))
print(type(users))
for key,value in users.items():
    print(key, ": ", value)