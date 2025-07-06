# Create a program that reads an array of integers and finds
# the second largest element in the array.


# prompt the user for the size of the array
n = int(input("Enter the size of the array: "))

# initialize an empty list to store the array elements
array = []

# read the elements of the array from the user
print("Enter the elements for the array: ")
for i in range(n):
    element = int(input(f"Enter element{i + 1}: "))
    array.append(element)

# initialize variable to store the largest and second largest elements
largest = array[0]
second_largest = array[0]

# find the largest and second largest elements
for element in array:
    if element > largest:
        second_largest = largest
        largest = element
    elif element > second_largest and element != largest:
        second_largest = element
    
# display the second largest element
print(f"Second largest element: {second_largest}")