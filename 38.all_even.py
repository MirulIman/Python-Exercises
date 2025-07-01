# Write a program that prints all even numbers from 1 to
# 100.

# Solution 1

# initialize variable to start at 1
num = 1

# use a while loop to iterate untill the number reaches 100
while num <= 100:
    if num % 2 == 0:
        print(num)
    num += 1


# Solution 2

# initialize a variable to start at 2
num = 2

# use a while loop to iterate untill the number reaches 100
while num <= 100:
    print(num)
    num += 2


# Solution 3

# use a for loop to iterate through the even numbers for 2 to 100
for num in range(2, 101, 2):
    print(num)