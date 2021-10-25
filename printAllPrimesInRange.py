lower = int(input("Enter the start of the range "))
upper = int(input("Enter the end of the range "))

for number in range(lower, upper + 1):
    # 1 is neither composite nor prime so ignore it
    if number == 1:
        continue
    # A number is prime if it is not divisible by any number
    # Logically, a number can only be divisible by a number less that itself and greater than 2
    # So iterate from 2 to the number that you are checking and if it is divisible by any number in the range then it is not prime
    
    # Assuming that the number is prime
    flag = True
    for i in range(2, number):
        if number % i == 0:
            # Control will come here if the number is not prime, so negating our assumption and breaking
            flag = False
            break
    # If the assumption is still true then the number is prime
    if flag == True:
        print("Un optimised output ", number)


# =========================METHOD 2====================
# The above program can be improved
# Consider a fact that a number can be perfectly divisible only by any number less than or equal to hald of it 
for number in range(lower, upper + 1):
    # 1 is neither composite nor prime so ignore it
    if number == 1:
        continue
    # Consider the loop for optimisation
    flag = True
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            # Control will come here if the number is not prime, so negating our assumption and breaking
            flag = False
            break
    # If the assumption is still true then the number is prime
    if flag == True:
        print("optimised output ", number)
