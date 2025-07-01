# Make a program that reads the age of three people and how many of them
# are of legal age (age 18 or older).

# prompt the user to enter the age of three people
age1 = int(input("Enter the age of the first person: "))
age2 = int(input("Enter the age of the second person: "))
age3 = int(input("Enter the age of the third person: "))

# initialize a variable to keep track of the count of legal age individual
legal_age_count = 0

# check if each person is legal age
if age1 >= 18:
    legal_age_count =+ 1
if age2 >= 18:
    legal_age_count =+ 1
if age3 >= 18:
    legal_age_count =+ 1

# display the count of legal age individual
print(f"Out of the three people, {legal_age_count} person is/are of legal age.")