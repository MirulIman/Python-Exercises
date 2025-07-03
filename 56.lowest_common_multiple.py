# Write a program that determines the lowest common
# multiple (LCM) between two numbers entered by the user.


# prompt the user for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# find the maximum of the two numbers
max = max(num1, num2)

# calculate the LCM
while True:
    if max % num1 == 0 and max % num2 == 0:
        lcm = max
        break
    max += 1

# display the LCM
print(f"LCM of {num1} and {num2} is {lcm}")