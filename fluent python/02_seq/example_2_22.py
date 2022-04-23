
import numpy as np

a = np.arange(12)

print(a)

print(type(a))

print(a.shape)
a.shape = 3, 4

print(a)

print(a[2])

print(a[:,1])

print(a.transpose())


result = """
[ 0  1  2  3  4  5  6  7  8  9 10 11]
<class 'numpy.ndarray'>
(12,)
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
[ 8  9 10 11]
[1 5 9]
[[ 0  4  8]
 [ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]]
"""
