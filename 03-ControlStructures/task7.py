###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
bonus = 0.15 # 15%
total_salary = 0
is_bonus = input ("Do you have a bounus? (Y/N)")


if is_bonus:
    total_salary = basic_salary + (basic_salary * bonus)
else:
   total_salary = basic_salary

print(f'Basic salary: {basic_salary} PLN')
print(f'Bonus included? {"Y" if is_bonus else "N"}')
print(f'Total salary: {total_salary} PLN')