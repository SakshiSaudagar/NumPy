import numpy as np

x= ([1, 2, 3, 4, 5])
y= np.array ([1, 2, 3, 4, 5])

print(y)
y
print(type(y))
print(y.ndim)

l= []
for i in range (1,10):
    int_l= int(input("Enter the number:"))
    l.append(int_l)

print(np.array(l))
print(l)

