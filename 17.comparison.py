# Write a program that reads two numbers and tells you which one is
# bigger.


# prompt the user for the first number
num1 = float(input("Enter the first number: "))

# prompt the user for the second number
num2 = float(input("Enter the second number: "))

# compare the numbers and determine the bigger one
if num1 > num2:
    print("The first number is bigger.")
elif num2 < num1:
    print("The second number is bigger.")
else:
    print("Both number are equal.")