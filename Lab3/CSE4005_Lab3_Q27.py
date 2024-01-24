# KHAN MOHD OWAIS RAZA
# 20BCD7138

#Q27]
import pandas as pd
import numpy as np
data = {'grps': ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'C'],
        'vals': [10, 8, 7, 4, 6, 3, 2, 1]}
df = pd.DataFrame(data)
def sum_of_three_greatest(group):
    sorted_values = group['vals'].sort_values(ascending=False)
    return sorted_values.head(3).sum()
result = df.groupby('grps').apply(sum_of_three_greatest)
print(result)
