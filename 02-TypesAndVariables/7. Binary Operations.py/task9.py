#In many games, the numbers one and six on dice have special meaning.
#  Write a program that prints the number of dice rolled and the value 
# True if the number rolled is 1 or 6. Sample result:



import random
dice_roll= random.randint(1,6)
special_meaning = dice_roll ==1 or dice_roll ==6
print(f'Dice rolled: {dice_roll}')
print(f'This roll dice has a special value:', {special_meaning})



