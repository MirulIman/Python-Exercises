# Write a program that asks the user for a number N and
# says whether it is prime or not (2, 3, 5, 7).


# prompt the user for a number
number = int(input("Enter a number: "))

# check if number is less than 2 (not prime)
if number < 2:
    is_prime = False
else:
    is_prime = True

    # check if the number is divisible by any integer
    # from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

# display the result
if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")