# Write a program that takes a full name and displays the last
# name (last name) first.


full_name = input("Enter your fullname: ")

# split the full name into a list of names
names = full_name.split()

# get the lastname for the list
last_name = names[-1]

print(f"Last name first: {last_name}")