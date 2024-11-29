# The distance to the horizon depends on the height of the observer above the ground. 
# The higher you are, the farther away the horizon is. For most situations, 
# you can use the following formula:

#d = 3.57 × √h

#Where:

#d is the distance to the horizon in kilometers
#h is the height of the observer in meters

#Write a program that calculates the distance to the horizon from a height given in meters from the keyboard. 
# Then, using the program, calculate the distance to the horizon in km when:

#You are standing on a beach, by the sea, on the water line (calculate the distance for your height in m). 16
#You are looking out of a hotel window located by the sea, the window is at a height of 20 meters.

import math 
height_m = float(input('Type your height in m:'))
distance_km = math.sqrt(height_m)*3.57
print("The distance to the horizon is:", round(distance_km, 2), "km")
