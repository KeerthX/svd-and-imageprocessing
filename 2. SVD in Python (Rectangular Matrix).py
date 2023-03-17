import numpy as np

# Define a rectangular matrix A
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Compute the SVD of A
U, s, VT = np.linalg.svd(matrix)

print(U)
print(s)
print(VT)

# We construct a diagnoal matrix using the following steps 

#Create a 0 Matrix with the same shape as our original matrix
S = np.zeros_like(matrix)

#Push the elements from the eigen value matrix diagnoally to the zero matrix
S[:min(matrix.shape), :min(matrix.shape)] = np.diag(s)

#Reconstruct the matrix using @ operator
new_matrix = U@s@VT

# Print the results
print("Original matrix A =\n", matrix)
print("Reconstructed matrix A_reconstructed =\n", new_matrix)