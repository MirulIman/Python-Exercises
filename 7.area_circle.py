# Write a program that calculates the area of a circle from the
# radius, using the formula A = πr²

import math

# prompt the user for thr radius
radius = float(input("Enter the radius of the circle: "))

# calculate the area
area = math.pi * radius ** 2

# display the result
print(f"The area of the circle is {area}")