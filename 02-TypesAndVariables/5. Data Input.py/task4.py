# 23% VAT was paid from an amount. Write a program that reads an amount from the keyboard. 
# Then, it calculates and prints both the amount and its VAT.
#  Apply formatting with two decimal places. Sample result:



amount = float(input("Enter the amount: "))
VAT= amount*0.23
print(f'The paid amount is : {amount:.2f}')
print(f'And it is VAT is : {VAT:.2f}')