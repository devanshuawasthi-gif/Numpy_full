# CHANGING THE SHAPE OF AN ARRAY

import numpy as np

a = np.floor(10*np.random.random((3,4)))
print(a)

print(a.shape)

print(a.ravel()) # return the array flattern

print(a.reshape(6,2)) # return the arrya in a modified shape

print(a.T)  # return the arrsay transposnded

print(a.T.shape)

print(a.shape)


# STACKING TOGETHER DIFFERENT ARRAYS
'''Several arrays can be stacked together along different axes:'''

a = np.floor(10*np.random.random((2,2)))
print(a)


b = np.floor(10*np.random.random((2,2)))
print(b)

print(np.vstack((a,b)))

print(np.hstack(a,b))



'''The function column_stack stacks 1D arrays as columns into a 2D array. It is equivalent to hstack only for 2D
arrays'''

from numpy import newaxis

print(np.column_stack((a,b)))


