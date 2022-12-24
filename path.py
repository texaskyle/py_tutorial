from pathlib import Path

"""path = Path("Ecommerce")
# returns a boolean
print(path.exists())"""

"""# creating a directory
path = Path("emails")
print(path.mkdir())"""

"""# removing a directory
path = Path("emails")
print(path.rmdir())"""

path = Path()
for file in path.glob('*.py'):
    print(file)
    print(type(file))


