# Create a program that prompts the user for a number and
# displays the table of that number using a loop.


# use a nested for loop to iterate through the range 1 to 11
# for both multiplicands
for i in range(1, 11):
    for j in range(1, 11):
        # calculate the product of the two numbers
        product = i * j

        # display the multiplication table entry
        print(j, 'X', i, '=', product)

    # print a separator between each multiplication table
    print("-" * 20)