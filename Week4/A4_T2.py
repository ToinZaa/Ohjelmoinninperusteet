#A4_T2 For-loop 2

#Copy the previous program and modify the behaviour to match the example program run below. This program must use “for-loop” structure.

#It is recommended to replace the print-command end character with space, so that all the iterations can be printed on the same row. Last iteration might require additional logic to get rid of the extra space at the end.

#Note! the autograding tool will test that the correct structure has been applied.

print("Program starting.")

num1 = int(input("\nInsert starting value: "))
num2 = int(input("Insert stopping value: "))

if num1 <= num2:
    print("\nStarting for - loop:")
    for i in range(num1, num2 + 1):
        print(i, end = ' ')
    print("\nProgram ending.")
    
else:
    print("\nProgram ending.")