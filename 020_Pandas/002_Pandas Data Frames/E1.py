"""
1. Write a Python program to get the powers of an array values element-wise. Go to the editor
Note: First array elements raised to powers from second array
Expected Output:
Original array
[0 1 2 3 4 5 6]
First array elements raised to powers from second array, element-wise:
[ 0 1 8 27 64 125 216]
"""

import pandas as pd

df = pd.Series([0, 1, 2, 3, 4, 5, 6])
df1 = df**3
print(df1)
