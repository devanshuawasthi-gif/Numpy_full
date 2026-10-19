#  One-dimensional arrays can be indexed, sliced and iterated over, much like lists and other Python sequences

import numpy as np

a = np.arange(10) ** 3
print(a)

print(a[2])

print(a[2:4])

print(a[:6:2])

print(a[: :-1])

for i in a:
    print(i ** (1/3.))
    
def f(x, y):
    return 10*x+y

b = np.fromfunction(f,(5,4),dtype=int)
print(b)

print(b[2,3])     ## each row in the second column of b

print(b[0:5,1])    

print(b[1:3, :])   ## each column in the second and third row of b