#A3_T4 More menu options

#Extend the previous menu program by adding three more options to the menu.

#Options:

#    Print the name backwards
#        Your name backwards is "{NameBackwards}"
#    Print the first character
#        The first character in name "{Name}" is "{FirstChar}"
#    Show the amount of characters in the name
#        There are {NameLength} characters in the name "{Name}"


#Program starting.
#This is a program with simple menu, where you can choose which operation the program performs.
#Before the menu, please insert your name: John

#Options:
#1 - Print welcome message
#2 - Print the name backwards
#3 - Print the first character
#4 - Show the amount of characters in the name
#0 - Exit
#Your choice: 1
#Welcome John!

#Program ending.


print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs")

Name = input("Before the menu, please insert your name: ")

print("\nOptions:")
print("1 - Print welcome message")
print("2 - Print the name backwards")
print("3 - Print the first character")
print("4 - Show the amount of characters in the name")
print("0 - Exit")

Choice = int(input("Your choice: "))

if Choice == 1:
    print(f"Welcome {Name}!")
elif Choice == 2:
    print(f'Your name backwards is "{Name[::-1]}"') # Käänteinen merkkijono
elif Choice == 3:
    print(f'The first character in name "{Name}" is "{Name[0]}"') # Ensimmäinen merkki
elif Choice == 4:
    print(f'There are {len(Name)} characters in the name "{Name}"') # Merkkien määrä
elif Choice == 0:
    print("Exiting...")

print("\nProgram ending")