# Write a program that takes a full name and displays only
# the first name.


full_name = input("Enter your fullname: ")

# split the full name into list of names
names = full_name.split()

# get first name from the list
first_name = names[0]

print(f"First name: {first_name}")