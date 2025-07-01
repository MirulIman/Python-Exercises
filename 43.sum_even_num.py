# Write a program that calculates and displays the sum of
# even numbers from 1 to 100 using a repeating loop.


# Solution 1

# initialize variables
sum_of_evens = 0
num = 2

# use a while loop to iterate until num reaches 100
while num <= 100:
    # add the current number to the sum if it is even
    sum_of_evens += num
    
    # increment the number by 2 to get the next even number
    num += 2

# display the sum of the even numbers
print(f"The sum of even numbers from 1 to 100 is {sum_of_evens}")


# Solution 2

# initialize variable
sum_of_evens = 0

# use a for loop with range and step 2 to iterate through even numbers
for num in range(2, 101, 2):
    sum_of_evens += num

# display the sum of even numbers
print(f"The sum of even numbers from 1 to 100 is {sum_of_evens}")