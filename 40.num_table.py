# Create a program that prompts the user for a number and
# displays the table of that number using a loop.

# Solution 1

# prompt the user for a number
number = int(input("Enter the number: "))

# use for loop to iterate through the range 1 to 12
for i in range(1, 13):
    # calculate the product of the number and current iteratiion value
    product = number * i

    # display the multiplication table entry
    print(i, "X", number, "=", product)


# Solution 2

# prompt the user for a number
number = int(input("Enter the number: "))

# initialize a counter variable
i = 1

# use a while loop to iterate until the counter reaches 12
while i <= 12:
    # calculate the product
    product = number * i

    # display the multiplication table entry
    print(i, "X", number, "=", product)

    # increment the counter by 1
    i += 1