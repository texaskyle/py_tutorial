import os
"""
# checking if a file or a folder exist plus the path to the file or a folder
# path = "C:\\Users\\charles\\Desktop\\text.txt.txt" #checking the location of the file
path = "C:\\Users\\charles\\Desktop\\New folder"
if os.path.exists(path):
    print('This path exists')
    if os.path.isfile(path):
        print('this is a file')
    elif os.path.isdir(path):
        print("this is a folder!")
else:
    print("This file doesn't exists")"""

"""# reading the contents of a file
try:
    with open("C:\\Users\\charles\\Desktop\\text.txt.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("This file was not found!!!")"""


"""text = "am in forth year!!"
with open('text.txt', 'w') as file:
    file.write(text)"""

"""statement = "using 'w' will overwrite the file!\n"
with open('text.txt', 'w') as file:
    file.write(statement)

sentence = "using 'a' wont overwrite the file"
with open('text.txt', 'a') as file:
    file.write(f"{sentence} \n it was nice knowing the using 'a' doesn't overwrite the file \n nice progress ")
    
with open('text.txt') as file:
    print(file.read())"""


"""
# copying a file
import shutil
shutil.copyfile('text.txt', 'text1.txt') # source, destination

with open('text1.txt') as file:
    print(file.read())"""

"""# moving the file into another path
# source = "C:\\Users\\charles\\Desktop\\rental management system.docx"
source = "text.txt"
destination = 'text2.txt'

try:
    if os.path.exists(destination):
        print("The path exist")
    else:
        os.replace(source, destination)
        print(f"{source} was moved to {destination}")

except FileNotFoundError:
    print("the file was not found")


with open('text2.txt') as file:
    print(file.read())"""

"""
# deleting a file
path = 'delete.txt'
try:
    os.remove(path)
except FileNotFoundError:
    print("The file you are attempting to delete is not found")"""


import shutil
# deleting a directory
# path_dir = 'empty_folder'
path = 'folder'
try:
     # os.rmdir(path) #removes only an empty file directory
    # shutil.rmtree(path) #removes the folder and its content
except PermissionError:
    print("You do not have the permission to delete this!!!")
except FileNotFoundError:
    print(f"You have already deleted {path}")
except OSError:
    print("You cannot delete that using that function")
else:
    print(f"{path} was successfully deleted!")








