
# Now this empty array is declared gloabally and is accessible everywhere
# ye islie kia hai kyuki input hum ek function me lege iss array ka
# and  bahar usko dusre function me use karke print karege
# top pe define kie jaate hai global variables taaki compiler pehle inhe padhe
# aur usse pata ho inke use se pehle ki esa kuch exist karta hai
arr = []

def printArrayReverse(length):
    for i in range(length - 1, -1, -1):
        # range(length - 1, -1, -1) isko samajhne ke lie
        # pehle ye samajh ki ulta print karne ke lie loop chalana hai last se front tak
        #  ab iske lie start index hoga -> last position in array
        #  jo hme length se pata hai array ki.... ab 0 based indexing hoti hai to agar 4 length ka array hai to
        # indexes hue 0 1 2 3 matlab 4 ni ayega kyuki 0 se start karke 4 length ke indexes 3 pe khatam hojaate hai
        # islie length - 1 se start karvaya loop
        # ab second cheez comma ke baad isme -1 likha hai ... vo ye batata hai ki jaana kaha tak hai decrement kar karke
        # ab -1 to koi index hota ni... but inhone -1 islie likha kyuki python reverse jaate hue end range me jo bhi do uske ek pehle tak chalta hai
        # matlab -1 se ek pehle matlab 0 tak chalega.. jese forward loop me hota hai
        #  and last vaala -1 loop ko bata rha hai ki har step pe 1-1 number kam karte chalo
        print(arr[i], end = " ")

def inputArray(length):
    for i in range(1, length + 1):
        element = int(input("Enter the number to be inserted "))
        arr.append(element)


length = int(input("Enter the length of the array "))
inputArray(length)
printArrayReverse(length)