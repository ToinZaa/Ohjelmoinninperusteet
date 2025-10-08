#A3_T6 Submenu (TEST TASK)

#Create menu program with submenus. Mainly for unit conversions. Use the values from the following table for unit conversions https://www.isa.org/getmedia/192f7bda-c77c-480a-8925-1a39787ed098/CCST-Conversions-document.pdf

#Menu options:

#    Length
#        Meters to kilometers
#        Kilometers to meters
#    Weight
#        Grams to pounds
#        Pounds to grams
#    Exit
#        “Exiting...”

#Handle all the data in floating point datatype. Remember to round every value in 1 digit precision right before displaying.

#Other possible prints:

#    “Unknown option.”

#Example run - weight conversion 1

print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.\n")

print("Options: ")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
Choice = int(input("Your choice: "))

if (Choice == 1):
    print("Length options: ")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")

    Choice2 = int(input("Your choice: "))
    if Choice2 == 1:
        meters = float(input("Insert meters: "))
        kilometers = meters / 1000
        print(f"{meters:.1f} m is {kilometers:.1f} km")
    elif Choice2 == 2:
        kilometers = float(input("Insert kilometers: "))
        meters = kilometers * 1000
        print(f"{kilometers:.1f} km is {meters:.1f} m")
    elif Choice2 == 0:
        print("Exiting...")
    else:
        print("Unknown option.")

elif(Choice == 2):
    print("\nWeight options: ")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")

    Choice2 = int(input("Your choice: "))
    if Choice2 == 1:
        grams = float(input("Insert grams: "))
        pounds = grams * 0.00220462
        print(f"{grams:.1f} g is {pounds:.1f} lb")
    elif Choice2 == 2:
        pounds = float(input("Insert pounds: "))
        grams = pounds / 0.00220462
        print(f"{pounds:.1f} lb is {grams:.1f} g")
    elif Choice2 == 0:
        print("Exiting...")
    else:
        print("Unknown option.")

elif Choice == 0:
    print("\nExiting...")

else:
    print("Unknown option.")

print("\nProgram ending.")