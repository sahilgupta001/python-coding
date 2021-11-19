arr = []

def printArr(length):
    for i in range(length):
        print(arr[i], end = " ");

def addOneToAlternate(length):
    # ab ye loop 2-2 ke steps lega forward direction me
    for i in range(0, length, 2):
        arr[i] = arr[i] + 1

def inputArray(length):
    for i in range(length):
        element = int(input("Enter the number to be inserted "))
        arr.append(element)


length = int(input("Enter the length of the array "))
inputArray(length)
addOneToAlternate(length)
printArr(length)
