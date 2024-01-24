# KHAN MOHD OWAIS RAZA
# 20BCD7138

#Q24]
import pandas as pd
import numpy as np
data = np.random.rand(5, 10)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
column_with_smallest_sum = df.sum().idxmin()
print("Column with the smallest sum:", column_with_smallest_sum)

