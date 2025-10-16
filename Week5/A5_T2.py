#A5_T2 Pass argument

#Create Python program which is able to print user input with a decorative frame.

#Program must consist of two functions:

#    main-function
#        Print starting and ending statements.
#        Print any empty row (see example program run)
#        Prompt user to insert a word.
#        Pass the inserted word into the frameWord-function.
#        Returns None
#    frameWord
#        Takes PWord as a parameter.
#        Prints the framing and the PWord
#            Hint: Multiply the asterisk '*'-character.
#        Returns None


def frameWord(PWord):
    #Kehyksen luonti
    border = '*' * (len(PWord) + 4)
    print(border)
    print(f"* {PWord} *")
    print(border)
    return None

def main ():
    print("Program starting.")
    print()
    word = input("Insert word: ")
    frameWord(word)
    print()
    print("Program ending")

main()



