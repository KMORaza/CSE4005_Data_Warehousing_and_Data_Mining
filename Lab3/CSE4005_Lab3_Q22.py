# KHAN MOHD OWAIS RAZA
# 20BCD7138

#Q22] You have a Data Frame df with a column 'A' of integers.
#     How do you filter out rows which contain the same integer as the row immediately above?
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 4, 5, 6, 6]})
filtered_df = df[df['A'] != df['A'].shift()]
print(filtered_df)
