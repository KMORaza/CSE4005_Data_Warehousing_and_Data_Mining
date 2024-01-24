# KHAN MOHD OWAIS RAZA
# 20BCD7138

#Q25] How do you count how many unique rows a Data Frame has (i.e. ignore all rows that are duplicates)?
#     As input, use a Data Frame of zeros and ones with 10 rows and 3 columns.
import pandas as pd
import numpy as np
data = np.random.randint(2, size=(10, 3))
df = pd.DataFrame(data, columns=['A', 'B', 'C'])
unique_rows_count = len(df.drop_duplicates())
print("Number of unique rows:", unique_rows_count)
