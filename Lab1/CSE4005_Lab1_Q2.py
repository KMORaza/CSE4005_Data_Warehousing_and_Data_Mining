# KHAN MOHD OWAIS RAZA
# 20BCD7138
# CSE4005 Lab-1, Q2
def reverse_digits(integer):
    reversed_str = str(integer)[::-1]
    for digit in reversed_str:
        print(digit, end=" ")
given_integer = 7536
reverse_digits(given_integer)
