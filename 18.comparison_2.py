# Write a program that asks the user for three numbers and displays the
# largest one.


# prompt the user for the three numbers
num1 = float(input("Enter the first number: " ))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# determine the largest number using conditional statements
if num1 >= num2 and num1 >= num3:
    largest_number = num1
elif num2 >= num1 and num2 >= num3:
    largest_number = num2
else:
    largest_number = num3

# display the largest number to the user
print(f"The largest number is {largest_number}")
