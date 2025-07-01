# Write a program that calculates the work done by a force
# acting on an object, using the formula T = F * d, where T is the
# work, F is the applied force, and d is the distance traveled by
# the object.


# prompt the user for the applied force and distance traveled
applied_force = float(input("Enter the applied force: "))
distance = float(input("Enter the distance traveled: "))

# calculate the work done
work_done = applied_force * distance

# display the result
print(f"The work done by the force is {work_done}")