# A5_T5 Menu-driven program

# Create a menu-driven Python program with following options:

#    Insert a word
#        Which stores user inserted word into memory.
#    Show current word
#        Prints the word from the memory
#   Show current word in reverse
#        Prints the word from the memory in reverse.
#    Exit
#        Stops the program gracefully
#    Unknown option

# Initialize the Word with an empty string.


def insertWord() -> str:
    word = input("Insert a word: ")
    return word

def showWord(currentWord: str) -> None:
    print(f"Current word - {currentWord}\n")
    return None
    

def showWordReverse(currentWord: str) -> None:
    reverseWord = currentWord [::-1]
    print(f"Word reversed - {reverseWord}\n")
    return None

def main():
    Word = ""
    print("Program starting.")
    while True:
        print("Options:")
        print("1. Insert word")
        print("2. Show current word")
        print("3. Show current word in reverse")
        print("0. Exit")
        Prompt = input("Your choice: ")
            
        if Prompt == "1":
            Word = insertWord()
        elif Prompt == "2":
            showWord(Word)
        elif Prompt == "3":
            showWordReverse(Word)
        elif Prompt == "0":
            print("Exiting program.")
            print("\nProgram ending.")
            break
        else:
            print("Unknown option")
main()



