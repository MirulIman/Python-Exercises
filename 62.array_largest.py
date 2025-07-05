# Write a program that reads an array of integers and
# displays the largest element in the array.


# prompt the user to enter the number of elements in the array
n = int(input("Enter the number of elements: "))

# initialize an empty list to store the elements
array = []

# read the elements from the user
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)

# initialize a variable to hold the largest element
largest = array[0]

# iterate over the element in the array
for i in range(1, n):
    if array[i] > largest:
        largest = array[i]

# display the largest element
print(f"The largest element in the array is {largest}")