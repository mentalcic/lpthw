from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

str1 = input("Enter some string here: ")
str2 = input("Enter something else here: ")

print(f"First you typed {str1} and you typed {str2} next")

# What's the difference between argv and input()?
# The difference has to do with where the user is required to give input.
# If they give your script inputs on the command line, then you use argv.
# If you want them to input using the keyboard while the script is running, then use input().
