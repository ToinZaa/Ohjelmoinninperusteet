# Make a Python program, which prompts the user name and two floating numbers.
# Multiply the inserted numbers to get product. Round the product in two decimal precision.
# Complete the program output as shown below.

# Example program run:

# program starting
# What is your name: John
# Enter a floating point number: 3.1
# Enter second floating point number: 5.3
# John you gave numbers 3.1 and 5.3
# Multyplying first and second number will result in product 16.43
# program ending

print("Program starting")
Name = input("What is your name: ")
First_number = input("Enter a floating point number: ")
First_number = float(First_number)

Second_number = input("Enter second floating point number: ")
Second_number = float(Second_number)
# Muutetaan syöte liukuluvuksi
print(f"{Name} you gave numbers {First_number} and {Second_number}")
# print f-stringillä

Multi = First_number * Second_number
print(f"Multiplying first and second number will result in product {round(Multi, 2)}")

print("Program ending")