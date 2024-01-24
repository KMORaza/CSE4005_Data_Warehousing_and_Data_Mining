# KHAN MOHD OWAIS RAZA
# 20BCD7138

#Q23]
import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.random(size=(5, 3)))
df_subtracted = df.sub(df.mean(axis=1), axis=0)
print("Original DataFrame:")
print(df)
print("\nDataFrame after subtracting row mean:")
print(df_subtracted)

