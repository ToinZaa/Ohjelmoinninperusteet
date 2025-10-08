#A4_T1 For-loop 1

#Create a Python program which prompts user to insert two integers. Use these integers together with the “for-loop” structure to create behaviour like in the example program example run below.

#Note! the autograding tool will test that the correct structure has been applied.

print("Program starting.")

num1 = int(input("\nInsert starting value: "))
num2 = int(input("Insert stopping value: "))

if num1 <= num2:
    print("\nStarting for - loop:")
    for i in range(num1, num2 + 1):
        print(i)
    print("\nProgram ending")
    
else:
    print("Program ending.")
