# ab iss code ko 2 functions me split karuga me
# ek function bhot basic hai jo sirf ek char ko check karega ki vo vowel hai ya ni
# dusra function karega baaki kaam
# aur ye function sirf small chars ka input lega esa assume karle

def checkVowel(character):
    # ek hi if me bhi kar sakte hai neeche vaala kaam but dikhne me acha lage islie kardia bas split
    if character == 'a' or character == 'e' or character == 'i':
        return True
    if character == 'o' or character == 'u':
        return True
    return False

def countVowels(word):
    count = 0
    for i in range(len(word)):
        if checkVowel(word[i]):
            count = count + 1
    return count

word = input("Enter the word that you want to check ")
count = countVowels(word)
print("Number of vowels are ", count)