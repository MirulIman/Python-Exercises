# Create a program that calculates and displays the perimeter
# of a circle, prompting the user for the radius.


import math

# prompt the user for the radius
radius = float(input("Enter the radius of the circle: "))

# calculate the perimeter
perimeter = 2 * math.pi * radius

# display the result
print(f"The perimeter of the circle is {perimeter}")