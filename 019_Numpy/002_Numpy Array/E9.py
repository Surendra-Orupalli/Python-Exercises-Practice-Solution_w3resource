"""
9. Write a Python program to add a border (filled with 0's) around an existing array.
Expected Output:
Original array:
[[ 1. 1. 1.]
[ 1. 1. 1.]
[ 1. 1. 1.]]
1 on the border and 0 inside in the array
[[ 0. 0. 0. 0. 0.]
[ 0. 1. 1. 1. 0.]
[ 0. 1. 1. 1. 0.]
[ 0. 1. 1. 1. 0.]
[ 0. 0. 0. 0. 0.]]
"""

import numpy as np

array = np.ones([3,3])
print(array)

array = np.pad(array, pad_width = 1, mode = 'constant', constant_values = 0)
print(array)
