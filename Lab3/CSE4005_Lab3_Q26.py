# KHAN MOHD OWAIS RAZA
# 20BCD7138

#Q26]
import pandas as pd
import numpy as np
data = np.random.random(size=(5, 10))
for row in data:
    np.random.shuffle(row)
    row[:5] = np.nan
df = pd.DataFrame(data, columns=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
def find_third_nan_column(row):
    nan_count = 0
    for col, value in enumerate(row):
        if pd.isna(value):
            nan_count += 1
            if nan_count == 3:
                return df.columns[col]
result_series = df.apply(find_third_nan_column, axis=1)
print(result_series)
