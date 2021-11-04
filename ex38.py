ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print("1")
print(stuff[1])
print("sveeee")
print(stuff)
print("-1")
print(stuff[-1])  # whoa! fancy
print("sveeeeeeee")
print(stuff)
print("popuj")
print(stuff.pop())
print("sveeee opet posle popa")
print(stuff)

print("popuj opet")
print(stuff.pop())
print("sveeee opet posle drugog popa")
print(stuff)


print(' '.join(stuff))  # what? cool!
print('#'.join(stuff[3:6]))  # super stellar!

print(stuff[2])
print(stuff[-2])
