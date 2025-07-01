# Make a program that asks for two numbers and displays if the first is
# divisible by the second


# prompt the user to enter the first and second number
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# check if the first number is divisible by the second number
if num1 % num2 == 0:
    result = "divisible"
else:
    result = "not divisible"

# display the result
print(f"The first number is {result} by the second number.")