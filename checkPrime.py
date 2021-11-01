def checkPrime(num):
    # ab dekhio isme ki seedha optimal part pe aaya hu me num/ 2 karke
    # last me dono solutions die the
    for i in range(2, num / 2):
        if num % 2 == 0:
            return False
    # ab ye control flow samajhna hai
    # samajh ki ye neeche vaala true kab execute hoga
    # yahan tak control kis case me ayega hi ni and kis case me ayega
    return True


num = int(input("Enter the number that you want to check "))

if checkPrime(num):
    print("The number is prime ")
else:
    print("The number is not prime")

