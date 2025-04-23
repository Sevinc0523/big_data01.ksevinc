import pandas as pd

s1 = pd.Series([10, 20, 30, 40], index=['w', 'x', 'y', 'z'])

result = s1[s1 > 20] / 10

print("20-dən böyük elementlərin 10-a bölünmüş halı:")
print(result)
