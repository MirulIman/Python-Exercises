# Create a program that reads an array of integers and
# checks that all elements are even.


# prompt the user for the size of the array
n = int(input("Enter the size of the array: "))

# initialize the array
array = []

# prompt the user for the elements of the array
for i in range(n):
    element = int(input(f"Enter the element {i+1}: "))
    array.append(element)

# check if all elements are even
is_even = True
for element in array:
    if element % 2 != 0:
        is_even = False
        break

# display the result
if is_even:
    print("All elements are even.")
else:
    print("Not all elements are even.")