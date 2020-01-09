# Accept two int values from the user and return their product.
# If the product is greater than 1000, then return their sum

# Expected output
# Enter first number 10
# Enter second number 20
# The result is 200


number1 = input("Enter first number: ")
number2 = input("Enter second number: ")
check = int(number1) * int(number2)
if check >= 1000:
    print("Posto je proizvod veci od 'iljadu zbir brojeva je: ", int(number1) + int(number2))
else:
    print("Proizvod je: ", check)
