# now this array is declared outside of the function
# So it will be accessible anywhere
# In previous questions it was declared inside inputArray function
# So we could not access it anywhere outside the function without passing a copy of it from inputArray function


arr = []

# We can assume that the maximum value in the array can be 1000

def findMinimumNumber():
    # ab ye iss logic ko khud se samajhne ka try kario
    # asaaan hai but likh ke karega tab aayega samajh
    # example le ek array ka jisme 1000 ya 1000 se choti values ho
    # fir ek variable rakh min_ele ka and chala ke dekh loop

    min_ele = 1001
    for num in arr:
        if num < min_ele:
            min_ele = num
    return min_ele

def inputArray(n):
    # declare an empty array

    # input the array
    for i in range(n):
        # create a temporary variable which will store the user input at any point
        temp = int(input())
        arr.append(temp)

    

n = int(input("Enter the size of the array "))
inputArray(n)
print(findMinimumNumber())