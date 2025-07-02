# Write a program that prompts the user for a list of
# numbers, until the user types the number zero, and displays the
# largest and smallest numbers in the list.


# initialize variables
largest = None
smallest = None

# read numbers from the user until zero is entered
while True:
    number = int(input("Enter a number (enter 0 to stop): "))

    # check if the number is zero
    if number == 0:
        break

    # check if the number is the largest or smallest so far
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

# display the largest and smallest numbers
if largest is not None and smallest is not None:
    print(f"The largest number is {largest}")
    print(f"The smallest number is {smallest}")
else:
    print("No numbers were entered.")