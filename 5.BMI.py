# Write a program that calculates the BMI of an individual,
# using the formula BMI = weight / height²


# prompt the user for the weight and height
weight = float(input("Enter the weight in kilograms: "))
height = float(input("Enter the height in meter: "))

# calculate the BMI
bmi = weight / (height ** 2)

# display the result
print(f"Your BMI is {bmi}.")