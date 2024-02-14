from itertools import combinations
def self_join(items, k):
    result = set()
    for combination in combinations(items, k+1):
        if any(set(combination).issubset(item) for item in result):
            continue
        result.add(combination)
    return result
input_data = [('a', 'b'), ('a', 'c'), ('b', 'c'), ('b', 'd'), ('c', 'd'), ('c', 'e'), ('c', 'f')]
output_data = self_join(input_data, 2)
print(output_data)
