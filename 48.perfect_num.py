# Create a program that displays the first N first perfect
# squares, where N is informed by the user, using a loop.


# prompt the user for a number
N = int(input("Enter the value of N: "))

count = 0 # initialize a counter to keep track of the number of perfect square found
num = 1 # start with the first positive integer

while count < N:
    square = num ** 2 # calculate the square of the current number

    # display the perfect square
    print(square, end = " ")
    count += 1

    num += 1 # move to the next number

# add a new line for better output formatting
print()