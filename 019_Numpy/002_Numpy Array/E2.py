"""
2. Write a Python program to convert a list of numeric value into a one-dimensional NumPy array. Go to the editor
Expected Output:
Original List: [12.23, 13.32, 100, 36.32]
One-dimensional numpy array: [ 12.23 13.32 100. 36.32]
"""

import numpy as np

list = [12.23, 13.32, 100, 36.32]
array = np.array(list)

print("List is", list)
print("Array is", array)
