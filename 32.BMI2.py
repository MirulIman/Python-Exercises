# Write a program that asks for a person's height and weight and calculates
# their body mass index (BMI), displaying the corresponding category
# (underweight, normal weight, overweight, obese, severely obese).


# prompt the user to enter their weight and height
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# calculate the BMI using the formula BMI = weight / height^2
bmi = weight / (height ** 2)

# determine the corresponding BMI category
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
elif bmi < 35:
    category = "Obese"
else:
    category = "Severly obese"

# display the bmi and category
print(f"Your BMI is {bmi}")
print(f"Category: {category}")