"""
7. Write a Python program to an array converted to a float type.
Sample output:
Original array
[1, 2, 3, 4]
Array converted to a float type:
[ 1. 2. 3. 4.]
"""

import numpy as np

array_int1 = np.array([1, 2, 3, 4])
print(array_int1)

array_float = array_int1.astype(float)
print(array_float)

array_int2 = array_float.astype(int)
print(array_int2)
