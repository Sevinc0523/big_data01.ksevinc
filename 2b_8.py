import pandas as pd

# List-dən DataFrame yaratmaq
data = [(1, 2), (3, 4)]
df1 = pd.DataFrame(data, columns=['A', 'B'])

# Sətir və sütun adlarını təyin etmək
df1.index = ['r1', 'r2']
df1.columns = ['c1', 'c2']

# Nəticəni çap etmək
print(df1)
