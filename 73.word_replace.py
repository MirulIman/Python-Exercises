# Create a program that takes a sentence and replaces all the
# letters "a" with "e".


sentence = input("Enter a sentence: ")

new_sentence = sentence.replace('a', 'e')

print(f"Modified sentence: {new_sentence}")

# OR 

new_sentence = ""
for letter in sentence:
    if letter == 'a':
        new_sentence += 'e'
    else:
        new_sentence += letter

print(f"Modified sentence: {new_sentence}")