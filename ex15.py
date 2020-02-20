# import argv functionality from sys package
from sys import argv
# define arguments
script, filename = argv
# open a filename and assign the returned file object to a variable
txt = open(filename)

# print the file name in a statement
print(f"Here's your file {filename}:")
# print the content of a file
print(txt.read())

# prints out another statement asking for a file name (again)
print("Type the filename again:")
# take the filename input from user and assign it to a variable
file_again = input("> ")
# open a filename and assign the returned file object to a variable
txt_again = open(file_again)
# print the content of a file
print(txt_again.read())
