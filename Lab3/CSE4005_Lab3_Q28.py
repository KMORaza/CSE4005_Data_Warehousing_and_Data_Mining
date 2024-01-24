# KHAN MOHD OWAIS RAZA
# 20BCD7138

#Q28]
import pandas as pd
import numpy as np
data = {'A': np.random.randint(1, 101, size=1000),
        'B': np.random.random(size=1000)}
df = pd.DataFrame(data)
bin_edges = np.arange(0, 101, 10)
df['group'] = pd.cut(df['A'], bins=bin_edges, labels=False)
result = df.groupby('group')['B'].sum()
print(result)
