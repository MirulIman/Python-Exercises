# Write a program that reads the x and y position of two
# points in the Cartesian plane, and calculates the distance
# between them.


import math

# prompt the user for the coordinates of point 1
x1 = float(input("Enter the x-coordinate of point 1: "))
y1 = float(input("Enter the y-coordinate of point 1: "))

#prompt the user for the coordinates of point 2
x2 = float(input("Enter the x-coordinate of point 2: "))
y2 = float(input("Enter the y-coordinate of point 2: "))

# calculate the disctance
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# display result
print(f"The distance between the two points is {distance}")