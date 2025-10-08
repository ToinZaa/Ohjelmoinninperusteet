#A3_T5 Temperature converter (TEST TASK)

#Create a temperature unit conversion program.
#Start the program by listing options for the user:

#    Celsius to Fahrenheit
#    Fahrenheit to Celsius
#    Exit

#Prompt user to insert choice. After the decision to convert, ask the amount of current temperature (use the floating point datatype). Lastly show the converted value to the user.
#For the unit conversions, use the formula Celsius = (Fahrenheit - 32) / 1.8
#Data representation examples:
#    50.0 °F
#    10.0 °C
#If the user chooses option Exit, notify the user: Exiting...
#Use 1 decimal precision to round the converted value.


#Program starting.

#Options:
#1 - Celsius to Fahrenheit
#2 - Fahrenheit to Celsius
#0 - Exit
#Your choice: 1
#Insert the amount of Celsius: 23
#23.0 °C equals to 73.4 °F

#Program ending.

print("Program starting.\n")
print("Options: ")
print("1 - Celcius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")

Choice = int(input("Your choice: "))

if Choice == 1:
    Celsius = float(input("Insert the amount of Celcius: "))
    Fahrenheits = Celsius * 1.8 + 32
    print(f"{round(Celsius,1)} °C equals to {round(Fahrenheits, 1)} °F")

elif Choice == 2:
    Fahrenheits = float(input("Insert the amount of Fahrenheit: "))
    Celsius = (Fahrenheits - 32) / 1.8
    print(f"{round(Fahrenheits,1)} °C equals to {round(Celsius,1)} °F")

elif Choice == 0:
    print("Exiting...")

else:
    print("Unknown option")

print("Program ending")



    

