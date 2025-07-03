# Rewrite the previous exercise code until the difference
# between the terms is less than 0.001.


import math

# prompt the user for the value of X
x = float(input("Enter the value of x: "))

term = 1.0
sum = 1.0
n = 1

while abs(term) >= 0.001:
    term *= x / n
    sum += term
    n += 1

# calculate e^x
math_result = math.exp(x)

# display the calculated result
print(f"Result (Custom Calculation): {sum}")
print(f"Result (math.exp): {math_result}")