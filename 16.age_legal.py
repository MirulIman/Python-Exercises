# Make a program that asks for a person's age and displays whether they
# are of legal age or not.


# prompt the user for their age
age = int(input("Enter your age: "))

# check if the person is of legal age
if age >= 18:
    print("You are of legal age.")
else:
    print("You are not of legal age.")