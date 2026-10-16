import numpy as np

# 1 Dimension array
arr1= np.array ([1, 2, 3, 4,])
print(arr1)
print(arr1.ndim)

# 2 Dimension array
arr2= np.array ([ [1, 2, 3, 4],
                 [1, 2, 3, 4] ])
print(arr2)
print(arr2.ndim)

# 3 Dimension array
arr3= np.array ([
                [[5, 6, 7],
                 [5, 6, 7],
                 [5, 6, 7] ]
                 ])
print(arr3)
print(arr3.ndim) 

# n Dimension array
arrn= np.array ([1,6,4,7,3] , ndmin = 10)
print(arrn)
print(arrn.ndim)