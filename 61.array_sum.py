# Create a program that reads an array of integers and
# displays the sum of all the elements..


# prompt the user for the number of elements in the array
n = int(input("Enter the number of elements: "))

# initialize an empty list to store the elements
array = []

# read the elements from the user
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)

# calculate the sum of the elements
sum = 0
for element in array:
    sum += element

# display the sum of the elements
print(f"The sum of the elements is: {sum}")

# OR

# prompt the user for the number of elements in the array
n = int(input("Enter the number of elements: "))

# initialize an empty list to store the elements
array = []

# read the elements from the user
i = 0
while i < n:
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)
    i += 1

# calculate the sum of the elements
sum = 0
i = 0
while i < len(array):
    sum += array[i]
    i += 1

# display the sum of the elements
print(f"The sum of the elements is: {sum}")