# A pallindrome is a word or a number which is same when read from left to right or from right to left
# Example :- NAMAN
# This is same when read from right to left and from left to right

word = input("Enter the word which is to be checked ")

# Logically if you think then this can be checked by comparing
# First character with last, similarly second character with second last character and so on
# All of them should be same
# try to understand what happens in case we have a string of odd length

# We will implement the above logic
start = 0
end = len(word) - 1

# Assuming that it is a pallindrome, similar to the print all primes function
is_pallindrome = True

while start < end:
    if word[start] != word[end]:
        is_pallindrome = False
        break
    start = start + 1
    end = end - 1

if is_pallindrome == True:
    print("Given string is a pallindrome")
else:
    print("Given string is not a pallindrome")