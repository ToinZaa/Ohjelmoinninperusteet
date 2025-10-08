#Make a program, which prompts user to insert words. Program must stop prompting words if user inserts empty word.
#After stopping the repetitive prompt, print the amount of words and characters that the user inserted.


print("Program starting.\n")

words = 0
chars = 0

while True:
    word = input("Insert a word: ")
    if word == "":
        break
    words += 1
    chars += len(word)

print(f"\nYou inserted:\n-{words} words\n-{chars} characters\n")

print("Program ending.")

