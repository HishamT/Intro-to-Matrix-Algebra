import numpy as np
A = np.array([[2,6,1], [1,2,-1], [5,7,-4]])
b = np.array([7,-1,9])
AInv = np.linalg.inv(A)
x = np.matmul(AInv, b)
print(x)

