# Write a Python program which asks user to insert hex color.
# In this case hex color is expected to be the 7 character representation
# starting with # and followed by 6 0-F characters to represent RGB colors.
# More about hex colors at https://en.wikipedia.org/wiki/Web_colors

#lice the amount of red, green and blue from that inserted color and display each color as shown below.


#Program starting.

#Insert a hex color: #FFA500

#Colors
#- Red FF
#- Green A5
#- Blue 00

#Program ending.

print("Program starting.\n")

hex_color = input("Insert a hex color: ")
red = hex_color[1:3]
# slicing, otetaan merkkijonosta osia
green = hex_color[3:5]
blue = hex_color[5:7]

print("\nColors")
print(f"- Red {red}")
print(f"- Green {green}")
print(f"- Blue {blue}\n")

print("Program ending.")