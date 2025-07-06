# Write a program that reads two arrays of integers with the
# same size and displays a new array with the elements resulting
# from the multiplication of the corresponding elements of the
# two arrays.


# prompt the user for the size of the arrays
n = int(input("Enter the size of the arrays: "))

# initialize the arrays
array1 = []
array2 = []

# prompt the user for the elements of the first array
for i in range(n):
    element = int(input(f"Enter the element {i+1} of the first array: "))
    array1.append(element)

# prompt the user for the elements of the second array
for i in range(n):
    element = int(input(f"Enter the element {i+1} of the second array: "))
    array2.append(element)  

# initialize the new array  
new_array = []

# multiply the corresponding elements of the two arrays
for i in range(n):
    product = array1[i] * array2[i]
    new_array.append(product)

# display the new array
print("The new array is: ", new_array)