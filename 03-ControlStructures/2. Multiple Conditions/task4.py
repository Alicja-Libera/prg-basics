
2 * 4
3 - 5
5 * 6
###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
import math

number1 = int(input("Enter first number"))
number2 = int(input("Enter 2nd nr:"))
operator = input("Enter math operator")


if operator == "+":
  score= number1+number2
elif operator == "-":
  score= number1-number2
elif operator =="*":
  score= number1*number2
elif operator == "/":
  score= number1/number2

print(f'The result is {score}')
