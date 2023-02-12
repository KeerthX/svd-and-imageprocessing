#In this project we will look at what the mathematical defenition of SVD is in python.

#We will be using the numpy library for performing SVD.

import numpy as np

#Consider any nxn matrix as they are the easiest to work with.

matrix = np.array([[1,1,1],[1,1,1],[1,1,1]])

#U represents the Left Singluar Matrix, s the eigne value matrix and, VT the right singluar matrix.
U,s,VT = np.linalg.svd(matrix)

print(U)
print(s)
print(VT)
