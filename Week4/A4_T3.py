#A4_T3 While-loop

#Make Python program which prompts user to insert two integers. Use these integers together with the “while-loop” structure to create behaviour like in the example program run below.

#Note! the autograding tool will test that the correct structure has been applied.


print("Program starting.\n")

num1 = int(input("Insert starting value: "))
num2 = int(input("Insert stopping value: "))

if num1 <= num2:
    i = num1
    while i <= num2:
        print(i, end=' ')
        i += 1
    print("Program ending.")
else:
    print("Program ending.")