from itertools import combinations
def generate_subsets(items):
    subsets = []
    for i in range(1, len(items) + 1):
        subsets.extend(combinations(items, i))
    return subsets
input_items = ['a', 'b', 'c']
output_subsets = generate_subsets(input_items)
print(output_subsets)
