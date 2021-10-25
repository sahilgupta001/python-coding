# Fibonacci has first two numbers fixed i.e 0 and 1
# After that every number in the sequence is the sum of previous two numbers


n = int(input("Enter the length of required fibonacci sequence "))

print("0")
if n == 1:
    exit()

print("1")
if n == 2:
    exit()

number_one = 0
number_two = 1

for i in range(2, n):
    curr_num = number_one + number_two
    print(curr_num)
    # try to understand the below mentioned lines
    number_one = number_two
    number_two = curr_num

