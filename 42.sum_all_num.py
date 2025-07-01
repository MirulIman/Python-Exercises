# Write a program that asks the user for a number N and
# displays the sum of all numbers from 1 to N.

# Solution 1

# prompt the user for a number
N = int(input("Enter a number: "))

# initialize a variable to hold the sum
sum_of_numbers = 0

# use a for loop to iterate from 1 to N (inclusive)
for num in range(1, N +1):
    # add the current number to the sum
    sum_of_numbers += num

# display the sum of the numbers
print(f"The sum of numbers from 1 to {N} is {sum_of_numbers}")


# Solution 2

# prompt the user for a number
N = int(input("Enter a number: "))

# initialize a variable to hold the sum
sum_of_numbers = 0
num = 1

while num <= N:
    # add the current number to the sum
    sum_of_numbers += num

    # increment the number
    num += 1

# display the sum of the numbers
print(f"The sum of numbers from 1 to {N} is {sum_of_numbers}")