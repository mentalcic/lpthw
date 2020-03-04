# write a script similar to the last exercise that uses
# read and argv to read the file you just created
from sys import argv

script, filename = argv

var1 = open(filename)

print(f"Filename is {filename}.")
# need to research about the " " character in
# first position of the file content read out
print(f"Content of a {filename} is:","\n", var1.read())
