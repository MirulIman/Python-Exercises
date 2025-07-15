# Write a program that reads a word and checks if it is a
# palindrome (if it can be read backwards the same way).


word = input("Enter a word: ")

reversed_word = word[::-1]

if word == reversed_word:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")


# OR

is_palindrome = True

length = len(word)
for i in range(length // 2):
    if word[i] != word[length - i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")