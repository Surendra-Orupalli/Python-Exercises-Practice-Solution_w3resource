"""
2. Write a Python program to convert a Panda module Series to Python list and its type.
"""

import pandas as pd

ds = pd.Series([2, 4, 6, 8, 10])
print(ds)

list = ds.tolist()
print(list)
print(ds.dtypes)
