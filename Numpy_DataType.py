# Data Type
import numpy as np 

# Integer
var = np.array([1,2,3,4])
print("Data Type :", var.dtype)
print()

# Float
var1 = np.array([1.1, 1.3, 1.5, 1.7])
print("Data Type :", var1.dtype)
print()

# String
var2 = np.array(['s', 'a', 'k', 's', 'h', 'i'])
print("Data Type :", var2.dtype)
print()

var = np.array([1, 2, 3, 'a', 'b', 'c'])
print("Data Type :", var.dtype)
print()
print()

# converting DataType
x = np.array([1, 2, 4, 5], dtype = np.int8)
x1= np.array([1, 2, 4, 5], dtype = 'f')

print("Data Type:", x.dtype)
print(x)

print("Data Type:", x1.dtype)
print(x1)
print()

# DataType used as a Function
x2= np.array([1, 2, 4, 5], dtype = 'f')

new = np.float32(x2)
new1 = np.int_(new)

print("Data Type:", x2.dtype)
print("Data Type:", new.dtype)
print("Data Type:", new1.dtype)

print(x2)
print(new)
print(new1)
print()

# Covert DataType using AS
y= np.array([ 1, 3, 4, 6])

z = y.astype(float)

print(y)
print(z)




