# Arithmatic Operations
import numpy as np

# 1D Array
var = np.array([1, 2, 3, 4])
var_add = var + 3

print(var_add)
print()

var1 = np.array([1, 2, 4, 5])
var2 = np.array([1, 2, 4, 5])
var_add = var1 + var2

print(var_add)
print()

var10 = np.array([1, 2, 4, 5])
var11 = np.array([1, 2, 4, 5])
var_add = np.add(var10 , var11)

print(var_add)
print()

var3 = np.array([1, 2, 3, 4])
var_add = var3 * 3

print(var_add)
print()

var4 = np.array([1, 2, 3, 4])
var_add = var4 / 3

print(var_add)
print()

# 2D Array
a = np.array([ 
    [1, 2, 3, 4],
    [1, 2, 3, 4]
    ])
b= np.array([
    [5, 6, 7, 9],
    [3, 6, 8, 5]
    ])

var_sub= a - b

print(var_sub)


