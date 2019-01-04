"""
4. Write a Python program to create a null vector of size 10 and update sixth value to 11.Go to the editor
[ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
Update sixth value to 11
[ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]
"""

import numpy as np

vector = np.zeros(10)
print(vector)
vector[5] = 11
print(vector)
