import pandas as pd

data = {'A': [1, 2], 'B': [3, 4]}
df2 = pd.DataFrame(data)

filtered_df = df2[df2['A'] > 1]

print(filtered_df)
