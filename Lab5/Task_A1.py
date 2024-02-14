from collections import Counter
def count_sets(key, data):
    key_set = frozenset(key)
    set_counts = Counter(frozenset(item) for item in data)
    return key, set_counts[key_set] if key_set in set_counts else 0
input_key = ('a', 'b', 'c')
input_data = [['a', 'b', 'c', 'd'], ['b', 'c', 'd'], ['b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e']]
result_key, count = count_sets(input_key, input_data)
print(f'{result_key} → {count}')
