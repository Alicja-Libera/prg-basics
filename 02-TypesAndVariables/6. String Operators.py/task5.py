#To improve readability, telephone numbers are often presented with a dash or space separating some digits.
#  Write a program that prints a 9-digit telephone number entered from the 
# keyboard as three groups of 3 digits each, separated by a dash character. Sample result:



###
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#
phone_number= input('Enter phone number: ')
formatted_number = phone_number[:3] + "-" + phone_number[3:6] + "-" + phone_number[6:]
print(f'Phone number: {formatted_number}')