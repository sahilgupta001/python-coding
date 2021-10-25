# Factorial of a number is the product of the number itself with all numbers less than it, upto 1
# Example : 
# 4! => 4 x 3 x 2 x 1 = 24
# 5! => 5 x 4 x 3 x 2 x 1 = 120

number = int(input("Enter the number whose factorial is to be found "))

# Variable to store the factorial of the number
fact = 1

for i in range(2, number + 1):
    fact = fact * i

print(fact)


