def checkPrime(num):
    # ab dekhio isme ki seedha optimal part pe aaya hu me num/ 2 karke
    # last me dono solutions die the
    for i in range(2, int(num / 2)):
        if num % 2 == 0:
            return False
    # ab ye control flow samajhna hai
    # samajh ki ye neeche vaala true kab execute hoga
    # yahan tak control kis case me ayega hi ni and kis case me ayega
    return True


num = int(input("Enter the number that you want to check "))

if num == 1:
    print("This is neigher prime nor composite")
    exit()

# try kario ye samajhne ka ki exit() likhne se kya change aaya
# 1 daalke dekhio input me iske lie
# hoga ye ki 1 dekhte hi compilter iss line ke neeche ki line pe jayega hi ni
# upar vaala if me ayega aur vahan hme jo dikhana hai vo dikhayege aur
# program se exit maardege

if checkPrime(num):
    print("The number is prime ")
else:
    print("The number is not prime")

