a = input("Enter the value of a ")
b = input("Enter the value for b ")

# Consider the dynamic formation of output string in the line below
print("The values entered by you of a is ", a, " and that of b is ", b)

# Swapping is to exchange the values of a and b
# If we just simply write a = b... this is not going to exchange the values,
# rather it is going to replace the value in a with b

# This can be solved using another empty varaible as a memory store
# First we save one variables value to this empty store (assume it to be s)
# assume we had a = 10 and b = 15 as two numbers
# save a's value to store -> s = 10
# Now we will not loose a's value as it is there in s
# Replace a's value with b's value, so now s = 10, a = 15 and b = 15
# Now the only step left is to replace b with a's value which is stored in s
# so a = 15 and b = 10

c = a
a = b
b = c

print("The swapped value a is ", a, " and that of b is ", b)

  