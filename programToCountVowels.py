str = input("Enter the word in which vowels are to be counted ")

count_vowels = 0

for character in str:
    if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
        count_vowels = count_vowels + 1
    elif character == 'A' or character == 'E' or character == 'I' or character == 'O' or character == 'U':
        count_vowels = count_vowels + 1

print("Number of vowels are ", count_vowels)