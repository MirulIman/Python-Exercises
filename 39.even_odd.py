# Write a program that displays even numbers 1 to 50 and
# odd numbers 51 to 100 using a repeating loop.


# initialize a variable to start at 1
num = 1

# use a while loop to iterate until the number reaches 100
while num <= 100:
    if num <= 50:
        if num % 2 == 0:
            print(num)
    else:
        if num % 2 != 0:
            print(num)
    num += 1