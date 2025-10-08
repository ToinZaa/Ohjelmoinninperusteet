#A4_T7 Multiplicative persistency (TEST TASK)

#Create program which prompts the user to insert an integer and then display the steps to calculate the multiplicative persistency based on the user input.

#In short, the steps in the multiplicative persistency is calculated by multiplying digits together in a given integer. This process is then repeated for the result which makes the result value smaller on each iteration till the result contains only one digit.

#The program must stop the iteration when the result contains only one digit. Finally before the program closes, it shows the steps taken.

print("Program starting.\n")
print("Check multiplicative persistence.")

number = int(input("Insert an integer: "))

steps = 0

while number >= 10:
    digits = [int(d) for d in str(number)]
    product = 1
    for d in digits:
        product *= d
    print(f"{' * '.join(str(d) for d in digits)} = {product}")
    number = product
    steps += 1
    
print("No more steps.\n")
print(f"This program took {steps} step(s)\n")
print("Program ending.")

