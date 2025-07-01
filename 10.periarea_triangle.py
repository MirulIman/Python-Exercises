# Write a program that calculates the perimeter and area of a
# triangle, using the formulas P = a + b + c and A = (b * h) / 2,
# where a, b and c are the sides of the triangle and h is the height
# relative to the side B.


# prompt the user for the lenght of the side and height of the trangle
side_a = float(input("Enter the lenght of side a: "))
side_b = float(input("Enter the lenght of side b: "))
side_c = float(input("Enter the lenght of side c: "))
height = float(input("Enter the heaight relative to side b: "))

# calculate the perimeter
perimeter = side_a + side_b * side_c

# calculate the area
area = (height * side_b) / 2

# display the result
print(f"Perimeter of the triangle: {perimeter}")
print(f"Area of the triangle: {area}")