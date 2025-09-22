#Make a Python program, which prompts for a compound word.

    # 1. Get following aspects from the word
        # 2. Length
        # 3. First character
        # 4. Reversed version e.g. “Suitcase” is reversed “esactiuS”
    # 2. Display the aspects using print commands.
    # 3. Prompt the user to take substring from the existing compound word.
    # 4. Finally print the user specified substring.

#Program starting.

#Insert a closed compound word: Moonbanana
#The word you inserted is 'Moonbanana' and in reverse it is 'ananabnooM'.
#The inserted word length is 10
#Last character is 'a'
#Take substring from the inserted word by inserting...
#1) Starting point: 0
#2) Ending point: 4
#3) Step size: 1
#The word 'Moonbanana' sliced to the defined substring is 'Moon'.
#Program ending.

print("Program starting.\n")

word = input("Insert a closed compound word: ")
reverse = word[::-1]
#::-1 tarkoittaa, että otetaan merkkijono alusta loppuun, mutta askel on -1 eli takaperin

print(f"The word you inserted is '{word}' and in reverse it is '{reverse}'.")

Length = (len(word))
print(f"The inserted word length is {Length}")

last = word[-1]

print(f"Last character is '{last}'\n")
print("Take substring from the inserted word by inserting...")

first = int(input("1) Starting point: "))
# määrää, mistä kohtaa merkkijono otetaan

second = int(input("2) Ending point: "))
# määrää, mihin kohtaan merkkijono otetaan

third = int(input("3) Step size: "))

complete = word[first:second:third]
print(f"\nThe word '{word}' sliced to the defined substring is '{complete}'.")

print("Program ending.")