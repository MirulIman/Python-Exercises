# Create a program that reads a word and displays the
# number of vowels present in it.


word = input("Enter a word: ")

# define a list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# initialize a variable to count the number of vowels
count = 0

# iterate over each character in the word 
for char in word:
    # check if the character is a vowel
    if char.lower() in vowels:
        count += 1


print(f"Number of vowels: {count}")