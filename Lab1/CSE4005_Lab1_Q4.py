# KHAN MOHD OWAIS RAZA
# 20BCD7138
# CSE4005 Lab-1, Q4
def count_characters(str1):
    chars_count = digits_count = symbols_count = 0
    for char in str1:
        if char.isalpha():
            if char.islower():
                chars_count += 1
            elif char.isupper():
                chars_count += 1
        elif char.isdigit():
            digits_count += 1
        else:
            symbols_count += 1
    return chars_count, digits_count, symbols_count
str1 = "P@#yn26at^&i5ve"
chars, digits, symbols = count_characters(str1)
print("Total counts of chars, digits and symbols:")
print(f"Chars = {chars}")
print(f"Digits = {digits}")
print(f"Symbol = {symbols}")


