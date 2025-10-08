# A4_T6 Collatz Conjecture (TEST TASK)

#Create a program which prompts the user to insert an integer and then display 
#the collatz conjecture as shown in the examples below.

print("Program starting.")

num = int(input("Insert a positive integer: "))

if num > 0:
    steps = 0
    print(str(num), end="")

    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num +1
        print(" -> " + str(num), end="")
        steps += 1

    print("\nSequence had " + str(steps) + " total steps.\n")

print("Program ending.")

