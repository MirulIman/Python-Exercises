# Write a program that determines the greatest common
# divisor (GCD) between two numbers entered by the user.


# prompt the user for numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# find the smaller of the two numbers
smaller = min(num1, num2)

# initialize the GCD variable
gcd = 1

# calculate the GCD
for i in range(1, smaller + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i

# display the GCD
print(f"GCD of {num1} and {num2} is {gcd}")


