# Write a program that prompts the user for two numbers and 
# displays the addition, subtraction, multiplication, and 
# division between them.


# prompt the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# perform arithmetic operation
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# display result
print("Addistion: ", addition)
print("Subtraction: ", subtraction)
print("Multipliaction: ", multiplication)
print("Division: ", round(division, 2))