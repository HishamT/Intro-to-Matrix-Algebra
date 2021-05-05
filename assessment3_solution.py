import numpy as np
# use this list when converting the encrypted characters to unicode.
s = ['ҿ', 'Ө', 'ѷ', 'Ӟ', 'Ͳ', 'Α', '̀', 'Ί'] # DO NOT copy and paste the characters.


E = np.array([[4,7],[3,5]])
D = np.linalg.inv(E)
y = np.array([[ord(s[0]), ord(s[1]), ord(s[2]), ord(s[3])],
              [ord(s[4]), ord(s[5]), ord(s[6]), ord(s[7])]])

x = np.matmul(D,y)
l = []
for i in range(0, 2):
    for j in range (0, 4):
        if(round(x[i][j]) == 0): # do not include padded zeros
            break
        l.append(chr(int(round(x[i][j]))))
print(l)

# the decrypted string is 'computer'