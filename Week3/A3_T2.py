#A3_T2 String comparisons

#Make Python program which does the following steps:

#    Prompt user to insert
#        A word
#        A character
#    Find if the character exists in the word. Possible prints below.
#        Word "{WordFirst}" contains character "{Character}"
#        Word "{WordFirst}" doesn't contain character "{Character}"
#    Prompt user to insert one more word
#    Compare the first word to the second word. Examples below:
#        The first word "{WordFirst}" is before the second word "{WordSecond}" alphabetically.
#        The second word "{WordSecond}" is before the first word "{WordFirst}" alphabetically.
#        Both inserted words are the same alphabetically, "{WordFirst}"

#   Program starting.
#   String comparisons
#   Insert first word: beans
#   Insert a character: n
#   Word "beans" contains character "n"
#   Insert second word: banana
#   The second word "banana" is before the first word "beans" alphabetically.
#   Program ending.

print("Program starting.")
print("String comparisons")

Sana1 = input("Insert first word: ")
Character = input("Insert a character: ")

if Character in Sana1:
    print(f'Word "{Sana1}" contains character "{Character}"')
else:
    print(f'Word "{Sana1}" doesn\'t contain character "{Character}"')

Sana2 = input("Insert second word: ")

if Sana1 < Sana2:
    print(f'The first word "{Sana1}" is before the second word "{Sana2}" alphabetically.')
elif Sana1 > Sana2:
    print(f'The second word "{Sana2}" is before the first word "{Sana1}" alphabetically.')
else:
    print(f'Both inserted words are the same alphabetically, "{Sana1}"')

print("Program ending.")