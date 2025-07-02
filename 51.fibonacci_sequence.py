# Write a program that prompts the user for a number and
# displays the Fibonacci sequence up to the given number using a
# repeating loop.


# prompt the user for a number
number = int(input("Enter a number: "))

# initialize variables
previous_number = 0
current_number = 1

# display the Fibonacci sequence up to the given number
print(f"Fibonacci sequence up to {number} is ")
print(previous_number, end=" ")

while current_number <= number:
    print(current_number, end=" ")

    # calculate the next fibonacci number
    next_number = previous_number + current_number

    # update the previous and current numbers
    previous_number = current_number
    current_number = next_number