# Import the library to use library functions for calculations

import math

# Here we are taking the string type input and conveting it to integer type in a single line of code
number = int(input("Enter the number whose square root is to be found "))

# This will give you a decimel number by default
squareRoot = math.sqrt(number)
print ("The square root of the givn number is ", squareRoot)


# We can use the round function to get the result rounded off to two decimal places
squareRoot = round(math.sqrt(number), 2)
print ("Rounded off square root of the number is ", squareRoot)


