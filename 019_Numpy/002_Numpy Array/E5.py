"""
5. Write a Python program to create a array with values ranging from 12 to 38.

Expected Output:
[12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]
"""

import numpy as np

for i in range(12, 38):
     array = np.array(i)
     i = i+1
     k = 0
     array = np.insert(array, k, [i])
     k = k+1

print(array)

print("---------------------------------")

import numpy as np
x = np.arange(12, 38)
print(x)
