import numpy as np

# w = 4, x = 5, y = 12, z = 8
A = np.array([[3,2,1,4],[1,4,2,3],[4,1,5,1],[1,1,1,1]])
b = np.array([66,72,89,29])
AInv = np.linalg.inv(A)
x = np.matmul(AInv,b)
print(x)


