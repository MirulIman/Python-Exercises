# Write a program that prompts the user for a number N and
# displays all prime numbers less than N.


# prompt the user for a number
n = int(input("Enter a number: "))

# iterate through numbers from 2 to n
for num in range(2, n):
    is_prime = True

    # check if the current number is divisible by any integer from 2
    # to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    # display the prime number
    if is_prime:
        print(num, end = " ")
    
# add a new line for better output formatting
print()