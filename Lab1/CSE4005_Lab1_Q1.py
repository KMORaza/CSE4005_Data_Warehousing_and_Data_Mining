# KHAN MOHD OWAIS RAZA
# 20BCD7138
# CSE4005 Lab-1, Q1
def calculate_income_tax(salary):
    if salary <= 500000:
        tax = 0
    elif salary <= 750000:
        tax = (salary - 500000) * 0.10
    elif salary <= 1000000:
        tax = 250000 * 0.10 + (salary - 750000) * 0.20
    else:
        tax = 250000 * 0.10 + 250000 * 0.20 + (salary - 1000000) * 0.30
    return tax
user_salary = int(input("Enter user's salary: "))
income_tax = calculate_income_tax(user_salary)
print(f'Tax to be paid: {income_tax}')
