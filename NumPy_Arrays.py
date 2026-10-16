import numpy as np

#Zeros
arr_zero = np.zeros(4)
arr_zero1 = np.zeros((3,4))
print(arr_zero)
print()
print(arr_zero1)

# Ones
arr_one = np.ones(5)
arr_one1 = np.ones((3,4))
print(arr_one)
print()
print(arr_one1)
print()

# Empty
arr_empty = np.empty (4)
print(arr_empty)
print()

# Range
arr_range = np.arange (4)
print(arr_range)
print()

# Diagonal
arr_dia = np.eye (3)
print(arr_dia)
print()

arr_dia1 = np.eye (3,5)
print(arr_dia1)
print()

# Linspace
arr_lin = np.linspace (0,10, num=5)
arr_lin1 = np.linspace (0,20, num=4)
print(arr_lin)
print()
print(arr_lin1)



