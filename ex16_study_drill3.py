# There is too much repetition in this file. Use strings,
# formats and escapes to print out line1, line2 and line3
# with just one target.write() command instead of six.

from sys import argv
# used test.txt for this script
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# not sure if I got it right
target.write(f"{line1}" + "\n" + f"{line2}" + "\n" + f"{line3}" + "\n")

print("And finally, we close it.")
target.close()