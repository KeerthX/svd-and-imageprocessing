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

#As you can see in this we get the eigen value matrix as a row matrix hence we use the diag function to make it diagonal 

s = np.diag(s)

print("---------------------------")

print(U)
print(s)
print(VT)

#We know that the matrices U, s, VT are factors of our matrix hence we can multiply these matrices and get our original matrix back

new_matrix = U@s@VT

print(new_matrix)

#Now lets try to find out the difference in their absolute values to calculate the error 

matrix_abs = np.absolute(matrix)
newmatrix_abs = np.absolute(new_matrix)

error = newmatrix_abs - matrix_abs

print("---------------------------")

print(error)

#As you can see the error is in the range of 10 raise to -16 which means the matrix we get after SVD is very close to the original matrix elements 