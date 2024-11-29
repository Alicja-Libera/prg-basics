#A SWIFT code (also known as BIC - Bank Identifier Code) is a unique identification 
# code used to identify a specific bank or financial institution globally. 
# It is primarily used for international wire transfers and communication between banks.

#SWIFT code is typically 8 or 11 characters long and is composed of the following elements:


###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.

swift = input('Enter SWIFT code: ')

# Extracting the first 4 characters as the Bank Code and the next 2 characters as the Country Code
bank_code = swift[:4]
country_code = swift[4:6]

# Printing the results
print(f'Bank Code: {bank_code}')
print(f'Country Code: {country_code}')
