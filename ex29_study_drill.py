# Study Drill 4.
# Can you put other Boolean expressions from Exercise 27 in the if-statement?
# Try it.

###################
print("\n\nExample 1:\n")

a1 = True
b1 = 1 != 0 and 2 == 1

print("Printing value of a1:", a1)
print("Printing value of b1:", b1)

if a1 != b1:
    print(f"{a1} is not equal to {b1}!")

if a1 == b1:
    print(f"{a1} is equal to {b1}!")

###################
print("\n\nExample 2:\n")

a2 = "chunky" == "bacon" and (not (3 == 4 or 3 == 3))
b2 = 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))

print("Printing value of a2:", a2)
print("Printing value of b2:", b2)

if a2 != b2:
    print(f"{a2} is not equal to {b2}!")

if a2 == b2:
    print(f"{a2} is equal to {b2}!")

###################
print("\n\nExample 3:\n")

# define variables
# define a procedure to nest some if statements
# and create a self loop like in main function from ex23
# execute the procedure to process the variables

# Next step is to
#  - ask user to input numbers a3 and b3
#  - ask for the increment
#  - ask for True of False

a3 = 10
b3 = 14
c3 = True
# Try with c3 = False :)


print(f"Value a3 = {a3}")
print(f"Value b3 = {b3}")
print(f"Value c3 = {c3}")
print("\n")


def compare_variables(a3, b3, c3):
    if a3 < b3:
        print(f"{a3} is less than {b3}.")
    if a3 == b3:
        print(f"{a3} is equal to {b3}.")
    if a3 > b3:
        print(f"{a3} is greater than {b3}.")
    if c3 != (a3 == b3):
        print(f"{not c3}! I do not comply! Move! On with it!")
    if c3 == (a3 == b3):
        print(f"{not c3}, I agree with this!")
        return print(f"Values are a3 = {a3} and b3 = {b3}. Value c3 = {c3} now looks important.")
    print("Adding more value to the first one")
    a3 += 1
    print(f"Values are a3 = {a3} and b3 = {b3}. Do not pay attention to value c3 = {c3}")
    return compare_variables(a3, b3, c3)


compare_variables(a3, b3, c3)
