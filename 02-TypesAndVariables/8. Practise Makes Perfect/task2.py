###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#
import math 

celcius= int(input("enter the degees in Celcius :"))
kelvin= celcius+273.15
Fahrenheit= 9/5+celcius + 32
print(f'The temperature in Celcius is : {celcius}')
print(f'The temperature in Kelvin is : {kelvin}')
print(f'The temperature in Fahrenheite is : {Fahrenheit}')
