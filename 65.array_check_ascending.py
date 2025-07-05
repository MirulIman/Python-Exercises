# Write a program that reads an array of integers and checks
# if they are in ascending order


# prompt the user for the number of elements in the array
n = int(input("Enter the number of elements: "))

# initialize an empty list to store the elements
array = []

# array of elements
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)

# check if the elements are in ascending order
is_ascending = True
for i in range(1, n):
        is_ascending = False
        break

# display the result
if is_ascending:
    print("The elements are in ascending order.")
else:
    print("The elements are not in ascending order.")