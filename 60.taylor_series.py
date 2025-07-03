# Make a program that calculates the value of sine using the
# Taylor series according to the equation below until the
# difference between the terms is less than 0.0001.


import math

# prompt the user for the angle in radians
angle = float(input("Enter the angle in radians: "))

term = angle
sum = angle
n =3

while abs(term) >= 0.0001:
    term *= - (angle ** 2) / ((n - 1) * n)
    sum += term
    n += 2

# calculate the sine
math_result = math.sin(angle)

# display the calculated result
print(f"Result (Custom Calculation): {sum}")
print(f"Result (math.sin): {math_result}")