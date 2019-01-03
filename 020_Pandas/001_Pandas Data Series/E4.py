"""
4. Write a Python program to get the largest integer smaller or equal to the division of the inputs. Go to the editor
Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
"""

import pandas as pd

ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 10])

print(ds1 == ds2)
print(ds1 < ds2)
print(ds1 > ds2)
