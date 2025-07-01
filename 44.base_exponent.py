# Write a program that calculates and displays the value of
# the power of a number entered by the user raised to an
# exponent also entered by the user, using repetition loops.


# prompt the user for the base number and the exponent
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

# initialize the result variable to hold the calculated value
result = 1

# use a for loop to iterate from 1 to exponent
for _ in range(1, exponent + 1):
    # multiply the result by the base number in each iteration
    result *= base

# display the calculated result
print(f"The result of {base} raised to the power of {exponent} is {result}")