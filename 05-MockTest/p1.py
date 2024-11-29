#(p1.py) The vending machine accepts 1, 2 and 5 PLN coins. Define the function f(amount_to_pay) that returns the
#minimum number of coins that can be used to pay for the purchased product. Sample result.

#f(23) returns 6
#f(8) returns 3


def f(amount_to_pay):
    count = 0
    for coin in [5, 2, 1]:
        count += amount_to_pay // coin
        amount_to_pay %= coin
    return count

# Test cases
print(f(23))  # 6
print(f(8))   # 3

def f(amount_to_pay):
 count =0
 for coin in [5,2,1]:
  count += amount_to_pay // coin
  amount_to_pay %=coin
 return count

print(f(23))
print(f(8))

