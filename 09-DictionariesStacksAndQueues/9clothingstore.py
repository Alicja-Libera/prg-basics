price_list = {
      'T-shirt': 19.99,
      'Jeans': 49.99,
      'Jacket': 89.99,
      'Sneakers': 59.99,
      'Hat': 15.99
   }
#prints a list of products and their prices before the discount

for key,value in price_list.items():
    print(f" {key} : {value}")

# prints the total value of the products before the discount

total_value_before_dis= sum(price_list.values())
print(f"The total value of the products before the discount is : {total_value_before_dis}")

# modifies the price list according to the discount (round prices to two decimal places)

discount_rate= 0.9
for key in price_list:
    price_list[key] = round((price_list[key]*discount_rate),2)

# prints a list of products and their prices after the 10% discount

for key, value in price_list.items():
    print(f" {key}: {value:.2f}")

#prints the total value of thea products after the discount
total_value_after_discount = sum(price_list.values())
print(f"\nThe total value of the products after the discount is: ${total_value_after_discount:.2f}")