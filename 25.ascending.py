# Make a program that reads three numbers, and displays them on the
# screen in ascending order.


# prompt the user to enter three numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third numeber: "))

# check the order of the numbers using if statements
if number1 <= number2 and number1 <= number3:
    if number2 <= number3:
        print(f"The numbers in ascending order are {number1} {number2} {number3}")
    else:
        print(f"The numbers in ascending order are {number1} {number3} {number2}")

elif number2 <= number1 and number2 <= number3:
    if number1 <= number3:
        print(f"The numbers in ascending order are {number2} {number1} {number3}")
    else:
        print(f"The numbers in ascending order are {number2} {number3} {number1}")

else:
    if number1 <= number2:
        print(f"The number in ascending order are {number3} {number1} {number2}")
    else:
        print(f"The number in ascending order are {number3} {number2} {number1}")


# OR


# prompt the user to enter three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# create a list to store the numbers
num_list = [num1, num2, num3]

# sort the list in ascending order
num_list.sort()

# display the numbers in ascending order
print(f"The numbers in acsending order are {num_list}")
print(f"The numbers in decsending order are {num_list[::-1]}")