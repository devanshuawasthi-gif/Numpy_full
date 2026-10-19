'''Splitting one array into several smaller ones
Using hsplit, you can split an array along its horizontal axis, either by specifying the number of equally shaped
arrays to return, or by specifying the columns after which the division should occur'''

import numpy as np

a = np.floor(10*np.random.random((2, 12)))
print(a)

#split a into 3
print(np.hsplit(a, 3))

#  split a after the third and the fourth coloumn
print(np.hsplit(a, (3, 4)))