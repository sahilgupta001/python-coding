
# Part 1
# string form me input ese lete hai... kyuki python me bydefault sab string me padha jaata hai
input1 = input("Enter a non decimal and we will convert it to int ")
# sample input = 123
input1 = int(input1)
print("Converted to int ", input1)
# output will be 123 after above conversion

# next two lines sirf thoda khula dikhane ke lie empty prints
print()
print()

# Part 2
input2 = input("Enter a decimal and we will convert it to float ")
# sample input = 123.12
input2 = float(input2)
print("Converted to float ", input2)
# output will be 123.12 after above conversion

print()
print()

# Part 3
input3 = input("Enter a decimal and we will convert it to int ")
# sample input = 123.12
input3 = int(float(input3))  #isme float hata ke dekh compiler error dega direct int conversion pe... ye language specific cheez hai ratne vaala kaal.... c++ khud karleta hai internally python ni karta
print("Converted to int ", input3)
# output will be 123 after above conversion (truncate kardega int conversion point ke aage ka automatically)

print()
print()

# Part 4
input4 = input("Enter a non decimal and we will convert it to float ")
# sample input = 123
input4 = float(input4)
print("Converted to float ", input4)
# output will be 123.00 after above conversion (truncate kardega int conversion point ke aage ka automatically)


