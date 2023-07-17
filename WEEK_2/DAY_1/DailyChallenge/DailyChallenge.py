# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.
# If it’s 10 characters, print a message which states “perfect string” and continue the exercise.

# Then, print the first and last characters of the given text.

# Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed.
# Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method).

sentence = input("Please, write a short string \n")

if len(sentence) < 10:
    print("the string is not long enough")
elif len(sentence) == 10:
    print("Perfect string")
else:
   print("The string is too long") 

print("First character is", sentence[0], "Last character is", sentence[-1])

new_string = ""
char = "4"

for char in sentence:
    new_string += char
    print(new_string)


import random

characters_list = list(sentence)
random.shuffle(characters_list)
shuffled_string = "".join(characters_list)
print("shuffled", shuffled_string)