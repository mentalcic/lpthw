# Take the file from the following url
# https://learnpythonthehardway.org/python3/exercise26.txt
# and fix it!
# Below is the fixed file. Original is provided in .txt form

from sys import argv  # missing import statement

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()  # missing line
print("How much do you weigh?", end=' ')  # missing )
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

script, filename = argv

txt = open(filename)  # spelling 'filenme'

print(f"Here's your file {filename}:")  # missing f in front of "
print(txt.read())  # tx. instead of txt

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())  # txt_again_read()


print('Let\'s practice everything.')  # missing escape \ in front of '
# line below was split in two lines here |
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love 
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")  # missing " on end
print(poem)
print("--------------")  # missing " on start


five = 10 - 2 + 3 - 6  # missing number 6 at end
print(f"This should be five: {five}")  # missing ) at end


def secret_formula(started):  # missing : at end
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100  # missing /
    return jelly_beans, jars, crates


start_point = 10000
jelly_beans, jars, crates = secret_formula(start_point)  # variables listed before = were beans and jars

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {jelly_beans} beans, {jars} jars, and {crates} crates.")  # beans instead of jelly_beans

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)  # typing error startpoint
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

people = 20
cats = 30  # spelling cates
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!") # missing ( and )

if people > cats:  # typing error (!?) < instead of >
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:  # missing : at end
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:  # missing : at end
    print("People are less than or equal to dogs.")  # missing " at end of string


if people := dogs:  # missing : in front of =
    print("People are dogs.")
