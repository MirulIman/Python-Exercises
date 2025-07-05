# Create a program that reads two vectors of integers of the
# same size and displays a new vector with the sum of the
# corresponding elements of the two vectors.


# prompt the user for the size of the vectors
n = int(input("Enter the size of the vectors: "))

# initialize two empty lists to store the vectors
vector1 = []
vector2 = []

# read the elements of the first vector from the user
print("Enter the elements of the first vector:")
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    vector1.append(element)

# read the elements of the second vector from the user
print("Enter the elements of the second vector:")
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    vector2.append(element)

# initialize an empty list to store the sum of the vectors
sum_vector = []

# calculate the sum of the corresponding elements of the vectors
for i in range(n):
    sum_vector.append(vector1[i] + vector2[i])

# display the sum vector
print("The sum vector is:", sum_vector)