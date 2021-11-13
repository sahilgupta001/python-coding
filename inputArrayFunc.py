
def printArray(arr : list):
    for num in arr:
        print(num, end = " ")


def inputArray(n):
    # declare an empty array
    arr = []

    # input the array
    for i in range(n):
        # create a temporary variable which will store the user input at any point
        temp = int(input())
        arr.append(temp)

    # Now trying to print this array by passing a copy of the array
    printArray(arr)


n = int(input("Enter the size of the array "))
inputArray(n)