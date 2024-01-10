# KHAN MOHD OWAIS RAZA
# 20BCD7138
# CSE4005 Lab-1, Q5
def calculate_sum_and_average(str1):
    digits = [int(char) for char in str1 if char.isdigit()]
    if digits:
        total_sum = sum(digits)
        average = total_sum / len(digits)
        return total_sum, average
    else:
        return 0, 0
str1 = "English = 78 Science = 83 Math = 68 History = 65"
total_sum, average = calculate_sum_and_average(str1)
print(f"Sum is {total_sum} and average is {average}")
