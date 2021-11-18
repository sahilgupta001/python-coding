
# ye return karne ka demo hai
def findGreaterType1(num1, num2):
    if num1 > num2:
        return num1
    # ab yahan pe iss line ke baad chahe to me else laga ke return kar sakta tha
    # but logically soch agar num1 num2 se bada hai to upar hi function se return hojayega
    # aur agar chota ya barabar hai tabhi neeche ayega right ?
    # ab else ki kya need hai kyuki hme pata hi hai yahan pe control tabhi ayega jab num2 bada ya barabar hai
    # seedha ans return kardo which is num2
    return num2

# ye return karne ka demo hai
def findGreaterType2(num1, num2):
    if num1 > num2:
        print(num1, "is greater")
        return
    print(num2, " is greater")


num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))

if num1 == num2:
    print("Numbers are equal")
    exit()

# ye function return kar rha hai ans islie usko catch karne ke lie ek variable me store kia jiska naam greater hai
greater = findGreaterType1(num1, num2)
print("By method 1 the output is ")
print(greater, " is greater")


# ab ye function andar hi apna kaam kardega print karne ka to islie need ni catch karne ki
print("By method 2 the output is ")
findGreaterType2(num1, num2)

# No need to print anything kyuki function kardega vo kaam 