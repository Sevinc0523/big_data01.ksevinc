import pandas as pd

# Dictionary-dən DataFrame yaratmaq
data = {'A': [1, 2], 'B': [3, 4]}
df2 = pd.DataFrame(data)

# 'A' sütununda 1-dən böyük olan sətirləri seçmək
filtered_df = df2[df2['A'] > 1]

# Nəticəni çap etmək
print(filtered_df)
