import numpy as np

a = np.arange(6)
print(a)        #--> 1d array

b = np.arange(12) .reshape(4,3)   #--> 2d array
print(b)

b = np.arange(12)   #--> 2d array without shape
print(b)

c = np.arange(24).reshape(2,3,4)  #---> 3d array
print(c)

print(np.arange(10000))

print(np.arange(10000).reshape(100,100))