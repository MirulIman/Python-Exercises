# Write a program that asks for the name of a day of the week and displays
# whether it is a weekday (Monday to Friday) or a weekend day (Saturday and
# Sunday).


# prompt the user to enter the name of a day
day = input("Enter the name of a day: ")

# convert the input to lowercase for case-insensitive comparison
day = day.lower()

# check if the day is weekday or weekend day
if day == 'saturday' and day == 'sunday':
    result = ("Weekend day")
else:
    result = ("Weekday")

# display the result
print(f"{day.capitalize()} is a {result}.")