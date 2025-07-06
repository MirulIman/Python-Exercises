# Write a program that reads an array of integers and
# displays how many times a specific number appears in the
# array


# prompt the user for the size of the array
n = int(input("Enter the size of the array: "))

# initialize an empty list to store the array elements
array = []

# read the elements of the array from the user
print(f"Enter elements for the array: ")
for i in range(n):
    element = int(input(f"Enter the element {i +1}: "))
    array.append(element)

# prompt the user for the number to count
num = int(input("Enter the number to count: "))

# initialize a variable to keep track of the count
count = 0

# iterate over the elements in the array
for element in array:
    # check if the current element is the number to count
    if element == num:
        count += 1

# display the count
print(f"The number {num} appears {count} times in the array.")