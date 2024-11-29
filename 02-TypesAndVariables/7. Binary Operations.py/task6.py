# The speed of vehicles on a highway in Poland must be between 40 and 140 km/h. 
# Write a program that checks whether the vehicle speed entered from the keyboard is correct.
#  Sample result:



Speed = int(input("Enter speed : "))
valid = Speed > 40 and Speed < 140
print(f'Speed is valid : {valid}')