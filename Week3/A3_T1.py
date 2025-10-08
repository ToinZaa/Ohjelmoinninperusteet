#Make Python program and implement if-statements in proper places.
#
#    Ask user to insert two integers
#    Compare the integers and then announce the greater number
#    Create sum of the two integers
#    Check the parity of the sum (see modulo-operator ‘%’)

#Other possible output variants:

#    Integer comparison
#        Integers are the same.
#        First integer is greater.
#    Parity check
#        Sum is even.


#   Program starting.
#Insert two integers.
#Insert first integer: 5
#Insert second integer: 5
#Comparing inserted integers.
#Integers are the same

#Adding integers together
#5 + 5 = 10

#Checking the parity of the sum...
#Sum is even.
#Program ending.


print("Program starting.")
print("Insert two integers.")

first = int(input("Insert first integer: ")) # käyttäjän syöte on aina string, joten se täytyy muuttaa int:iksi
second = int(input("Insert second integer: "))

print("Comparing inserted integers.")

if first > second: # vertailut ja jossittelut
    print("First integer is greater.\n")

elif first < second:
    print("Second integer is greater.\n")

else:
    print("Integers are the same.\n")

print("Adding integers together")

sum = first + second

print(f"{first} + {second} = {sum}")
print("\nChecking the parity of the sum...")

if sum % 2 == 0:
    print("Sum is even.")
else:
    print("Sum is odd.")

print("\nProgram ending.")

