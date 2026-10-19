# basic operations in NUMPY 

import numpy as np

a= np.array([20, 30, 40, 50])
b = np.arange(4)
print(a)
print(b)

c = a - b
print(c)

print(b**2)

print(10*np.sin(a))

print(a>35)


'''Unlike in many matrix languages, the product operator * operates elementwise in NumPy arrays. The matrix product
can be performed using the @ operator (in python >=3.5) or the dot function or method:'''

A = np.array( [[1,1],
 [0,1]] )
B = np.array( [[2,0],
 [3,4]] )

print(A * B)  # element wise product

print(A @ B) # matrix product

print(A.dot(B))    # Another matrix product




'''Some operations, such as += and *=, act in place to modify an existing array rather than create a new one'''

import numpy as np

a = np.ones((2, 3), dtype=int)  # Create a 2×3 array filled with 1

b = np.random.random((2, 3))  # Create a 2×3 array with random decimal values

a *= 3  # Multiply every element of a by 3
print(a)  # Print the updated a

b += a  # Add a to b and store the result in b
print(b)  # Print the updated b



'''Many unary operations, such as computing the sum of all the elements in the array, are implemented as methods of
the ndarray class'''

a = np.random.random((2,3))
print(a)

print(a.sum())

print(a.min())

print(a.max())



# UNIVERSAL FUNCTION
'''NumPy provides familiar mathematical functions such as sin, cos, and exp. I'''

B = np.array(3)
print(B)

print(np.exp(B))

print(np.sqrt(B))

C = np.array([2., -1., 4.])
print(np.add(B, C))