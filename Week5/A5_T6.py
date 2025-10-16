#A5_T6 Tally counter (TEST TASK)

#Make a menu-driven Python program which mimics Tally Counter.

#This menu-driven program must contain a maintainable program structure with the following requirements:

#    main function which represents the main program logic including menu cycle.
#    showOptions function which takes no arguments, shows the available options in the standard output and returns None.
#    askChoice function which takes no arguments, prompts user to insert choice and returns an integer regardless of the user feed.

#In case user incorrectly inserts text as a choice, the program must output "Unknown option!". For this, see the string method isnumeric() behaviour described in W3S or via Python documentation.

#See other requirements in the example program runs below.



def showOptions():
    print("Options:")
    print("1. Show count")
    print("2. Increase count")
    print("3. Reset count")
    print("0. Exit")
    return None

def askChoice() -> int:
    choice = input("Your choice: ")
    if choice.isnumeric():
        return int(choice)
    else:
        return -1

def main():
    counter = 0
    print("Program starting.")
    while True:
        showOptions()
        choice = askChoice()
        
        if choice == 1:
            print(f"Current count - {counter}")
        elif choice == 2:
            counter += 1
            print("Count increased!")
        elif choice == 3:
            counter = 0
            print("Cleared count!")
        elif choice == 0:
            print("Exiting program.")
            print("\nProgram ending.")
            break
        else:
            print("Unknown option!")

main()