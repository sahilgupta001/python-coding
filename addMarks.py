
# global empty dictionary
marks = {}

def calculateSum():
    sum = 0
    for student_name in marks:
        sum = sum + marks[student_name]
    print(sum)

def inputMarks(n):
    for i in range(n):
        name = input("Enter the name of the student ")
        score = int(input("Enter the score of the student "))
        # ab dictionary me enter karvayege
        marks[name] = score


n = int(input("Enter the number of students "))
inputMarks(n)
calculateSum()