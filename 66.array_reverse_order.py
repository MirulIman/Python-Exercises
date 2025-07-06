# Write a program that reads an array of integers and
# displays the elements in reverse order.


# prompt the user for the size of the array
n = int(input("Enter the size of the array: "))\

# initialize an empty list to store the array elements
array = []

# read the elements of the array from the user
print(f"Enter elements for the array: ")
for i in range(n):
    element = int(input(f"Enter the element {i +1}: "))
    array.append(element)

# invert the array using loop
start = 0
end = n - 1
while start < end:
    # swap the elements at the start and end positions
    array[start], array[end] = array[end], array[start]
    start += 1
    end -= 1

# OR 

# reverse the array using slicing
# reversed_array = array[::-1]

# display the elements in reverse order
print(f"Element in reverse order: ")
for element in array:
    print(element)


# OR

# display the elements in reverse order
# print(f"Element in reverse order:")
# for i in range(n - 1, -1, -1):
#     print(array[i])