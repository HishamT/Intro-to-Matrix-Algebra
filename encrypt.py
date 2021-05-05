import numpy as np

E = np.array([[9,3],[2,1]]) # encryption matrix
D = np.linalg.inv(E) # decryption matrix
x = np.array([[ord('h'), ord('e'), ord('l'), ord('l'), ord('o'), ord(' ')],
[ord('w'), ord('o'),ord('r'), ord('l'), ord('d'), 0]])
# "hello world" converted to unicode
y = np.matmul(E,x) # encryption
q = np.matmul(D,y) # decryption

print(q) # output q

'''
This outputs:

[[1.04000000e+02 1.01000000e+02 1.08000000e+02 1.08000000e+02
  1.11000000e+02 3.20000000e+01]
 [1.19000000e+02 1.11000000e+02 1.14000000e+02 1.08000000e+02
  1.00000000e+02 2.84217094e-14]]
'''


l = []

for i in range(0, 2):
    for j in range (0, 6):
        if(round(q[i][j]) == 0):
            break
        l.append(chr(int(round(q[i][j]))))
print(l)

'''
This outputs:

['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
'''