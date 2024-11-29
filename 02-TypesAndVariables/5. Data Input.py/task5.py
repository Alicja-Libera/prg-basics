#The price of the product on the price tag is given before and after the discount is applied. 
# Write a program that allows you to enter the product price and discount. 
# Print the product price, discount, discounted product price, and the 
# difference between the product price before and after the discount. 
# Print all prices with two decimal places. Sample result:



price= float(input("Enter the product's prize: "))
discount= float(input("Enter the given discount in %: "))
reduction=price * (discount / 100)
price_with_discount=price-reduction

print(f'The product price is: {price:.2f}, and the discount: {discount:.2f} %')
print(f'Price with discount is: {price_with_discount:.2f}, and the reduction is: {reduction:.2f}')