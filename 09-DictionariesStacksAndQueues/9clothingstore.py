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
for key,value in price_list.items():
    print(f"{key} : {value:.2f}" )

price_list= value*0.9 
print(f"The value afther discount is : {price_list}")