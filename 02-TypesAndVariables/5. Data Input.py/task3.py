#Write a program that calculates the volume and surface area of ​​a cuboid with sides a, b, and c. 
# Then, check the program for the following data:

#a = 3, b = 4, c = 5 --> volume = 94, surface area = 60
#a = 8, b = 1, c = 2 --> volume = 16, surface area = 52

###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#


a = int(input("a is: "))
b = int(input("b is: "))
c = int(input("c is: "))


cuboid_volume=a*b*c
print(f"Your cuboid volume is {cuboid_volume}")
surface=a*b*2+a*c*2+b*c*2
print(f"Your cuboid surface area is: {surface}")


...