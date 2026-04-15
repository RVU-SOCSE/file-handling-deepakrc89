import numpy as np
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

addition = A + B
print("\nAddition of matrices:")
print(addition)

multiplication = np.dot(A, B)
print("\nMatrix Multiplication:")
print(multiplication)

transpose_A = A.T
print("\nTranspose of Matrix A:")
print(transpose_A)
