# Write a program that prompts the user for two numbers A
# and B and displays all numbers between A and B.


# prompt the user for the two number
A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))

# determine the starting and ending values for the loop
start = min(A, B)
end = max(A, B)

# OR
# if A <= B:
#     start = A
#     end = B
# else:
#     start = B
#     end = A

# use a for loop to iterate over the number
# between A and B (inclusive)
for num in range(start, end + 1):
    print(num, end = " ")

# add a new line for better output formatting
print()