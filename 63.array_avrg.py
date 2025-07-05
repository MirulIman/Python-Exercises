# Write a program that reads an array of integers and
# displays the average of the elements.


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

# calculate the average
average = sum / n

# display the average
print(f"The average of the elements is {average}")