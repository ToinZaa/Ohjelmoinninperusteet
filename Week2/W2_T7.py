#Create a Python program to convert Fahrenheit to Celcius. Round the Celsius to 1 decimal precision.

#Formula to calculate Celcius from Fahrenheit is (Fahrenheit - 32) / 1.8

#Program starting.
#Insert fahrenheits: 50
#50.0°F is 10.0°C
#Program ending.

print("Program starting.")

fahrenheit = float(input("Insert fahrenheits: "))
celsius = (fahrenheit - 32) / 1.8   #Laskukaava

print(f"{fahrenheit}°F is {round(celsius, 1)}°C")  # round() funktio pyöristää desimaalin haluttuun kohtaan
print("Program ending.")