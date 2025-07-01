# Create a program that prompts the user for the radius of a
# sphere and calculates and displays its volume.


import math

# prompt the user for the radius of the sphere
radius = float(input("Enter the radius of the sphere: "))

# calculate the volume of the sphere
volume = (4 / 3) * math.pi *radius ** 3

# display the result to the user
print(f"The volume of the sphere is {volume}")