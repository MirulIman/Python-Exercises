# Write a program that calculates the average velocity of an
# object, using the formula v = Δs/Δt, where v is the average
# velocity, Δs is the space variation, and Δt is the time variation


# prompt the user for the space variation (Δs) and time variation (Δt)
space_variation = float(input("Enter the space variation (Δs): "))
time_variation = float(input("Enter the time variation (Δt): "))

# calculate the average velocity
average_velocity = space_variation / time_variation

# display the result
print(f"The average velocity is {average_velocity}")