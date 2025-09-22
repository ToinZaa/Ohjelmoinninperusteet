# Make Python program, which prompts user to insert two words. Print the length of each word and then compound them together. Put single quotes around the compound word.

# Example program run:

# Program starting.
# Insert first word: fire
# Insert second word: fighter
# 1st word is 4 characters long.
# 2nd word is 7 characters long.
# Words together makes one closed compound 'firefighter'.
# Program ending.

print("Program starting.")

First_word = input("Insert first word: ")
Second_word = input("Insert second word: ")

print(f"1st word is {len(First_word)} characters long.")
print(f"2nd word is {len(Second_word)} characters long.")
# len() funktio laskee merkkijonon pituuden

Compound = First_word + Second_word

print("Words together makes one closed compound ", f"{Compound}", sep="\'", end="\'.\n")
print("Program ending.")

