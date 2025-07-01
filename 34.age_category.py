# Create a program that asks for a person's age and displays whether they
# are a child (0-12 years old), teenager (13-17 years old), adult (18-59 years old),
# or elderly (60 years old or older).


# prompt the user to enter theit age
age = int(input("Enter your age: "))

# check the age range and assign the corresponding category
if age <= 12:
    category = "Child"
elif age <= 17:
    category = "Teenager"
elif age <= 59:
    category = "Adult"
else:
    category = "Elderly"
    
# display the category
print(f"You are a {category}")