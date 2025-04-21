import pandas as pd

# Dictionary-dən Series yaratmaq
data = {'p': 5, 'q': 10, 'r': 15}
s2 = pd.Series(data)

# 'q' indeksli elementi seçmək
element_q = s2['q']

# Nəticəni çap etmək
print("s2['q'] =", element_q)
