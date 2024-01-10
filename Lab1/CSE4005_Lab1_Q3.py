# KHAN MOHD OWAIS RAZA
# 20BCD7138
# CSE4005 Lab-1, Q3
num_elements = int(input("Enter the number of elements in the list: "))
list1 = []
for i in range(num_elements):
    element = int(input(f"Enter the {i}th element: "))
    list1.append(element)
result = []
for number in list1:
    if number % 5 == 0:
        result.append(number)
        if number > 150:
            break
print("The elements are:", " ".join(map(str, result)))

