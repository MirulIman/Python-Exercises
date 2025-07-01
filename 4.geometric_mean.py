# Write a program that calculates the geometric mean of three
# numbers entered by the user


import math

# prompt the user for three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# calculate the geometric mean
product = num1 * num2 * num3
geometric_mean = math.pow(product, 1/3)

# display the result
print("Geometric mean: ", geometric_mean)