# Assignment:
# Accept two int values from the user and return their product.
# If the product is greater than 1000, then return their sum
#
# Expected output
# Enter first number 10
# Enter second number 20
# The result is 200

# Solution
#
# def multiplication_or_sum(num1, num2):
#   product = num1 *num2
#   if(product < 1000):
#     return product
#   else:
#     return num1 +num2
#
# number1 = int(input("Enter first number "))
# number2 = int(input("Enter second number"))
#
# result = multiplication_or_sum(number1, number2)
# print("The result is", result)


number1 = input("Enter first number: ")
number2 = input("Enter second number: ")
check = int(number1) * int(number2)
if check >= 1000:
    print("Posto je proizvod veci od 'iljadu zbir brojeva je: ", int(number1) + int(number2))
else:
    print("Proizvod je: ", check)
