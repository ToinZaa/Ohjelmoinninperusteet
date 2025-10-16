#Create a Python program with two functions:

#    main-function
#        Does the routines ("Program starting." and "Program ending.")
#        Utilizes askName-function.
#        Utilizes greetUser-function.
#        Returns None
#    askName-function
#        Prompts the user to insert name
#        Returns name
#    greetUser-function
#        Which takes PName as an argument
#        Greets the user "Hello {PName}!"
#        Returns None


def askName():
    name = input("Insert name: ")
    return name

def greetUser(PName):
    print (f"Hello {PName}!")
    return None

def main():
    print("Program starting.")
    user = askName()
    greetUser(user)
    print("Program ending.")
    return None

main()