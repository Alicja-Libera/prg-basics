# A tree may be cut down if its diameter is at least 50 cm. 
# Write a program that, based on the circumference of the tree entered from the keyboard, 
# calculates and prints the value True if the tree can be cut down, 
# or print the value False otherwise. Sample result:


import math

circumference = int(input("Enter tree circumference in cm: "))
diameter = circumference / math.pi  # Obliczamy średnicę
requirement = diameter >= 50  # Sprawdzamy, czy średnica jest wystarczająca

print(f'Tree can be cut down: {requirement}')
