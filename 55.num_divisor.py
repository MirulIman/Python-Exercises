# Write a program that prompts the user for a number and
# displays its divisors


# prompt the user for a number
number = int(input("Enter a number: "))

# display the divisors of the number
print(f"The divisors of {number} are: ")
for i in range(1, number + 1):
    if number % i == 0:
        print(i)