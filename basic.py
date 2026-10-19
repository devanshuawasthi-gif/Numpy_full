import numpy as np
a = np.arange(15).reshape(3, 5)
print(a)

print(a.shape)  # number of rows and col

print(a.ndim)  # number of dimension of array

print(a.dtype.name) # datatype of array aelement

print(a.itemsize)  # size of each element in the array

print(a.size)  # total number of elements in the array

print(type(a)) # tyoe of the array