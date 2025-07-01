# Make a program that reads the year of birth of a person and informs if he
# is able to vote (age greater than or equal to 16 years old).


import datetime

# prompt the user to enter the year of birth
year_of_birth = int(input("Enter the year of birth: "))

# calculate the current year
current_year = datetime.datetime.now().year

# calculate the age of the person
age = current_year - year_of_birth

# check if the person is eligible to vote
print(age)
if age >= 16:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote yet.")