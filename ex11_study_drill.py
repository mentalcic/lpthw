varijabla = input("Upisi nesto: ")
print("Upisa ga ti za sve pare -", varijabla)
#print(type(varijabla))
#tip = type(varijabla)



try:
    val = int(varijabla)
    print("Input is an integer number. Number = ", val)
except ValueError:
    try:
        val = float(varijabla)
        print("Input is a float number. Number = ", val)
    except ValueError:
      print("No.. input is not a number. It's a string")
