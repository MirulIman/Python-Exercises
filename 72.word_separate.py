# Write a program that takes a word and displays each letter
# separately.


word = input("Enter the word: ")

for letter in word:
    print(letter)


# OR
print("*" * 10)

index = 0

while index < len(word):
    letter = word[index]
    print(letter)
    index += 1