def calculateSum(arr : list):
    sum = 0
    for num in arr:
        sum += num
    return sum

def calculateProduct(arr : list):
    prod = 1
    for num in arr:
        prod *= num
    return prod

def sumProduct(n):
    # declare an empty array
    arr = []

    # input the array
    for i in range(n):
        # create a temporary variable which will store the user input at any point
        temp = int(input())
        arr.append(temp)

    # Another functio which calculates the sum of the array that is passed to it
    arraySum = calculateSum(arr)
    # Similarly calling a function for multiplication
    productOfArray = calculateProduct(arr)

    # Now we need to return arraySum + productOfArray
    return arraySum + productOfArray

n = int(input("Enter the size of the array "))
print(sumProduct(n))