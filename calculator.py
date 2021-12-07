def printMenu():
    print("1 Add")
    print("2 Subtract")
    print("3 Multiply")
    print("4 Divide")

def printSum(num1, num2):
    print("The sum is ", num1 + num2)

def printDifference(num1, num2):
    print("The difference is ", num1 - num2)

def printProduct(num1, num2):
    print("The product is ", num1 * num2)

def printDivision(num1, num2):
    print("The answer after division is ", num1 / num2)

def calculator():
    doYouWantToCalculateMore = 'Y'
    
    while doYouWantToCalculateMore == "Y" or doYouWantToCalculateMore == 'y':
        num1 = int(input("Enter the first number "))
        num2 = int(input("Enter the second number "))
        choice = int(input("Enter the choice "))
        if choice == 1:
            printSum(num1, num2)
        elif choice == 2:
            printDifference(num1, num2)
        elif choice == 3:
            printProduct(num1, num2)
        else:
            printDivision(num1, num2)

        doYouWantToCalculateMore = input("Do you want to continue ? ")
    

calculator();