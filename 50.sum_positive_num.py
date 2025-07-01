# Write a program that reads numbers from the user until a
# negative number is entered, and prints the sum of the positive
# numbers.


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