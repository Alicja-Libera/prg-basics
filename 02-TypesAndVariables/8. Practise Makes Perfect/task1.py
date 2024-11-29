###
# Calculation of circle area and circumference 

import math
# determine radius and PI values
radius= int(input("Enter the value for radius :"))
# calculate area 
area= radius**2*math.pi
# calculate circumference 
diameter= radius*2
circumference= diameter*math.pi  
# print results
print(f'The area of the circle is:, {area:.2f}')
print(f'The circumference is:, {circumference:.2f}')
      