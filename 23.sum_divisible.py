# Make a program that reads three numbers, and informs if their sum is
# divisible by 5 or not.


# prompt the user to enter three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# calculate the sum of the three numbers
sum_of_numbers = number1 + number2 + number3

# check if the sum is divisible by 5
if sum_of_numbers % 5 == 0:
    print("The sum is divisible by 5.")
else:
    print("The sum is not divisible by 5.")