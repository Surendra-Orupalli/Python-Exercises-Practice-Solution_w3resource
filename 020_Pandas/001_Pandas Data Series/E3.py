"""
3. Write a Python program to add, subtract, multiple and divide two Pandas Series.
Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
"""

import pandas as pd

ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])

add = ds1 + ds2
print(add)

subtract = ds1 - ds2
print(subtract)

multiply = ds1 * ds2
print(multiply)

divide = ds1/ds2
print(divide)
