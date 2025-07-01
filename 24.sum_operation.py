# Create a program that reads three numbers and checks if their sum is
# positive, negative or equal to zero


# prompt the user to enter three numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

# calculate the sum of the three numbers
sum_of_numbers = number1 + number2 + number3

# check if the sum is positive, negative or zero
if sum_of_numbers > 0:
    print("The sum is positive.")
elif sum_of_numbers < 0:
    print("The sum is negative.")
else:
    print("The sum is zero.")