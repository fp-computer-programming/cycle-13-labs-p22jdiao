# Author: JD 03/07/2022

def factorial(number):
    result = 1
    if number != 0:
        # While the parameter does not equal to 0, the function will process as the n * (n-1)!
        result = number * factorial(number - 1)
        return result
    elif number == 0:
        return 1

print(factorial(5))
print(factorial(3))