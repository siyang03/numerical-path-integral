import cupy as cp

# Define the matrix
A = cp.array([[1, 2], [3, 4]])

# Compute the matrix power (e.g., A**3)
A_power = cp.linalg.matrix_power(A, 3)

print(A_power)