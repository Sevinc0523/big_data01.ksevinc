import pandas as pd

# s1 adlı Series-in yaradılması
s1 = pd.Series([10, 20, 30, 40], index=['w', 'x', 'y', 'z'])

# 20-dən böyük elementləri seçmək və 10-a bölmək
result = s1[s1 > 20] / 10

# Nəticəni çap etmək
print("20-dən böyük elementlərin 10-a bölünmüş halı:")
print(result)
