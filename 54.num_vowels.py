# Write a program that prompts the user for a sentence and
# displays the number of vowels in the sentence


# prompt the user for a sentence
sentence = input("Enter a sentence: ")

# initialize a counter variable
count = 0

# loop through each character in the sentence
for char in sentence:
    # convert to lowercase for case-insensitive comparison
    char = char.lower()

    # check if the character is a vowel
    if char in "aeiou":
        count += 1

# display the number of vowels
print(f"The number of vowels in the sentence is {count}")