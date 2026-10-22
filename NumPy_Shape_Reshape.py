# shape

import numpy as np

var = np.array ([[1,2], [1,4]])

print(var)
print()
print(var.shape)
print()

var1 = np.array ([1,2,3,4], ndmin=4)

print(var1)
print(var1.ndim)
print(var1.shape)
print()
print()

# Reshape

var2 = np.array ([1,3,4,5,6,7])
print(var2)
print(var2.ndim)
print()

x=var2.reshape(3,2)
print(x)
print(x.ndim)
print()

var3 = np.array ([1,3,4,5,6,7,5, 22, 11, 44,3,6])
print(var3)
print(var3.ndim)
print()

x1=var3.reshape(2,3,2)
print(x1)
print(x1.ndim)
print()

var4= np.array ([1,3,4,5,6,7,5, 22, 11, 44,3,6])
print(var4)
print(var4.ndim)
print()

x2=var4.reshape(2,3,2)
print(x2)
print(x2.ndim)
print()

one = x2.reshape(-1)
print(one)
print(one.ndim)
