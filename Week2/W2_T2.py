# Make a Python program, which prompts user for a car brand and model.
# After user inputs, do print the car brand and model sentence with two print commands using “sep” and “end” parameters.

# Example program run:

# program starting
# Insert car brand: Toyota
# Insert car model: Corolla
# Car brand is "Toyota" and the model is 'Corolla'.
# Program ending.
print("Program starting")

Brand = input("Insert car brand: ")
Model = input("Insert car model: ")

print(f"Car brand is ", f"{Brand}", sep="\"", end="\" ")
# sep lisää lainausmerkin ennen ja jälkeen merkkijonon
# end lisää lainausmerkin ja välilyönnin rivin loppuun
print(f"and the model is ", f"{Model}", sep="\'", end="\'.\n")
print("Program ending.")