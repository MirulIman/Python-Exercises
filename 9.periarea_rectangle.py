# Write a program that calculates the perimeter and area of a
# rectangle, using the formulas P = 2(w + l) and A = wl, where w
# is the width and l is the 


#prompt the user for the width and lenght of the rectangle
width = float(input("Enter the width of the rectangle: "))
length = float(input("Enter the lenght of the rectangle: "))

# calculate the perimeter
perimeter = 2 * (width + length)

# calculate the area
area = width * length

# display the result
print(f"Perimeter of the rectangle: {perimeter}")
print(f"Area of the rectangle: {area}")