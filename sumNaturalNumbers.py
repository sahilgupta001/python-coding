num = int(input("Enter the number upto which you need sum "))
sum = 0

while num > 0:
    sum += num
    num -= 1

print("Sum is ", sum)