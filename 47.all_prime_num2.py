# Create a program that displays the first N prime numbers,
# where N is informed by the user, using a loop


# prompt the user for a number
N = int(input("Enter the value of N: "))

count = 0
num = 2

while count < N:
    is_prime = True

    # check if the current number is divisible by any integer
    # from 2 to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime =False
            break
    
    # if the number is prime, display it
    if is_prime:
        print(num, end = " ")
        count += 1

    num += 1 # move the next number for checking

# add a new line for better output formatting
print()