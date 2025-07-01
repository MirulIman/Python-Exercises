# Write a program that calculates the delta of a quadratic
# equation (Δ = b² - 4ac)

# prompt the user for the coefficient of the quadratic equation
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# calculate the delta
delta = b ** 2 - 4 * a * c

# display the result
print(f"The delta of the quadratic equation is {delta}")