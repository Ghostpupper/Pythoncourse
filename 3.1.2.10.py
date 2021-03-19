# Prompt the user to enter a word
# and assign it to the userWord variable.
vovellessword = ''
userWord = input("Write a word:\n")
for letter in userWord:
    # Complete the body of the for loop.
    if letter == 'E' or letter == 'A' or letter == 'I' or letter == 'O' or letter == 'U': continue
    if letter == 'e' or letter == 'a' or letter == 'i' or letter == 'o' or letter == 'u': continue
    vovellessword += letter

print(vovellessword)
