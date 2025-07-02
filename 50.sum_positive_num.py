# Write a program that reads numbers from the user until a
# negative number is entered, and prints the sum of the positive
# numbers.

# Solution 1

# initialize varible 
sum_positive = 0

# read numbers from the user
while True:
    number = int(input("Enter a number (negative number to exit): "))

    # check if the number is positive
    if number >= 0:
        sum_positive += number
    else:
        break

# display the sum of positive numbers
print(f"Sum of positive numbers: {sum_positive}")



# Solution 2: without using break

# initialize variable
sum_positive = 0
number = 0

# read numbers from the user untill a negative number is entered
while number >= 0:
    number = int(input("Enter a number (negative number to exit): "))

    # check if the number is positive
    if number >= 0:
        sum_positive += number

# display the sum positive numbers
print(f"Sum of positive numbers: {sum_positive}")