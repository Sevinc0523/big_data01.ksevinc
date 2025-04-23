import pandas as pd

s1 = pd.Series([10, 20, 30, 40], index=['w', 'x', 'y', 'z'])

greater_than_25 = s1[s1 > 25]

print("25-dən böyük elementlər:")
print(greater_than_25)
