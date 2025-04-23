import pandas as pd

data = [(1, 2), (3, 4)]
df1 = pd.DataFrame(data, columns=['A', 'B'])

df1.index = ['r1', 'r2']
df1.columns = ['c1', 'c2']

print(df1)
