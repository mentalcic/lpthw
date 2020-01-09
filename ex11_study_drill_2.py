number1 = input("Enter first number: ")
number2 = input("Enter second number: ")
check = int(number1) * int(number2)
if check >= 1000:
    print("Posto je proizvod veci od 'iljadu zbir brojeva je: ", int(number1) + int(number2))
else:
    print("Proizvod je: ", check)
