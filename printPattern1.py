
# Now this empty array is declared gloabally and is accessible everywhere
# ye islie kia hai kyuki input hum ek function me lege iss array ka
# and  bahar usko dusre function me use karke print karege
# top pe define kie jaate hai global variables taaki compiler pehle inhe padhe
# aur usse pata ho inke use se pehle ki esa kuch exist karta hai
arr = []

def printArray(length):
    # ye first half ko normal print karne ke lie loop
    for i in range(int(length / 2)):
        print(arr[i], end = " ")
    
    for i in range(length - 1, int(length / 2) - 1, -1):
        print(arr[i], end = " ")

def inputArray(length):
    for i in range(1, length + 1):
        element = int(input("Enter the number to be inserted "))
        arr.append(element)


length = int(input("Enter the length of the array "))
inputArray(length)
printArray(length)