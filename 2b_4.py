import pandas as pd

data = {'p': 5, 'q': 10, 'r': 15}
s2 = pd.Series(data)

element_q = s2['q']

print("s2['q'] =", element_q)
