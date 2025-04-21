import pandas as pd

# List-dən DataFrame yaratmaq
data = [(1, 2), (3, 4)]
df1 = pd.DataFrame(data, columns=['A', 'B'])

# Nəticəni çap etmək
print(df1)
