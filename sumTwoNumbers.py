# Input functions for taking the input

a = input("Please enter the value for the first number ")
b = input("Please enter the value for the second number ")

sum1 = a + b #This is not going to give correct results as the inputs in python by default are strings

sum2 = int(a) + int(b) #Correct response

print(sum1, " is the wrong output")
print(sum2, " is the correcto output")