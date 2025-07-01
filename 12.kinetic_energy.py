# Write a program that calculates the kinetic energy of a
# moving object, using the formula E = (mv²) / 2, where E is the
# kinetic energy, m is the mass of the object, and v is the velocity.


# prompt the user for the mass and velocity of the object
mass = float(input("Enter the mass of the object: "))
velocity = float(input("Enter the velocity of the object: "))

# calculate the kinetic energy
kinetic_energy = (mass * velocity ** 2) / 2

# dislpay the result
print(f"The kinetic energy of the object is {kinetic_energy}")