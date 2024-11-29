
###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
bonus_input= input("Czy masz bonus? (tak/nie)")
is_bonus = bonus_input == 'tak' # does the employee receive a bonus
bonus = 0.30 # 15%

if is_bonus:
    total_salary = basic_salary * (1 + bonus)
else:
    total_salary= basic_salary

print(f'Basic salary: {basic_salary} PLN')
print(f'Bonus included? {"Yes" if is_bonus else "No"} PLN ')
print(f'Total salary: {total_salary} PLN ')
