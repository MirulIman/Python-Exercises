# Write a program that calculates the series below up to the
# tenth element


import math

# prompt the user for the value of x
x = float(input("Enter the value of x: "))

# initialize the sum and the term
sum = 1
term =1

# calculate the series up to the tenth elements
for n in range(1, 11):
    term *= x / n
    sum += term

# display the result
result = math.exp(x)
print(f"Approximation of e^x is {sum}")
print(f"Actual value of e^x is {result}")
