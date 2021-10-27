rows = int(input("Enter the number of rows "))
cols = int(input("Enter the number of columns "))


# Try to understand the below line
# [0] * cols this means that we need to create a row with cols number of zeros
# Now to tell how many such rows we need... we have used for i in range(rows)
# Tujhe ye samajh ni ayega but pura try kario samajhne ka
# Me to meet pe samjhauga hi isko

matrix = [[0] * cols for i in range(rows)]

# Printing the empty matrix

for i in range(rows):
    for j in range(cols):
        # try to remove end = " " and check how it changes the print format
        # isko ache se samajhio
        print(matrix[i][j], end = " ")
    print()