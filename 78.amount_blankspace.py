# Make a program that receives a sentence and displays the
# amount of blank spaces present in it.


sentence = input("Enter a sentence: ")

# initialize a variable to count the number of blank spaces
count = 0

for char in sentence:
    if char == " ":
        count += 1

print(f"Number of blank spaces: {count}")


# OR 

# use count() method to count the number of blank spaces
count = sentence.count(" ")

print(f"Number of blank spaces: {count}")