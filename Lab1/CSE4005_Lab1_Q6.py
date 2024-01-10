# KHAN MOHD OWAIS RAZA
# 20BCD7138
# CSE4005 Lab-1, Q6
def create_third_list(listOne, listTwo):
    odd_elements_list_one = [listOne[i] for i in range(1, len(listOne), 2)]
    even_elements_list_two = [listTwo[i] for i in range(0, len(listTwo), 2)]
    third_list = odd_elements_list_one + even_elements_list_two
    return odd_elements_list_one, even_elements_list_two, third_list
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
odd_elements, even_elements, third_list = create_third_list(listOne, listTwo)
print(f"Element at odd-index positions from list one: {odd_elements}")
print(f"Element at even-index positions from list two: {even_elements}")
print(f"Printing Final third list: {third_list}")
