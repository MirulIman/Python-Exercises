# Write a program that reads numbers from the user until
# zero is entered, and displays the average of the numbers
# entered.


# initialize variables
total = 0
count = 0

# read numbers from the user until zero is entered
while True:
    number = int(input("Enter a number (enter 0 to stop): "))

    # check if the number is zero
    if number == 0:
        break

    # add the number to the total and increment the count
    total += number
    count += 1

if count > 0:
    average = total / count
    print(f"Average: {average}")
else:
    print("No numbers were entered.")