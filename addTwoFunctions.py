# Program me input parts neeche hua karege abse and funtions upar
# aur ye sirf ese hi ek format follow karne ke lie

# def just informs the compiler ki hum ek user defined function likhne vaale hai

def sumTwo(num1, num2):
    # ye upar die hue num1 and num2 se koi khaas farak ni padta... kuch bhi rakho apne aap value aajayegi
    # next ques me aur clear karduga ye cheez example se
    sum = num1 + num2
    print("Sum of the given two numbers is ", sum)



num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))
# Now we can call the function to do rest of the work
sumTwo(num1, num2)
