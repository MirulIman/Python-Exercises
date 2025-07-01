# Write a program that reads three numbers and tells you if they can be the
# sides of a triangle (the sum of two sides must always be greater than the third
# side).


# prompt the user to enter three numbers
side1 = float(input("Enter the lenght of the first side: "))
side2 = float(input("Enter the lenght of the second side: "))
side3 = float(input("Enter the lenght of the third side: "))

# check if the three side are can form a triangle
if side1+side2 > side3 and side1+side3 > side2 and side2+side3 > side1:
    print("The three sides can form a triangle.")
else:
    print("The three side connot form a triangle.")