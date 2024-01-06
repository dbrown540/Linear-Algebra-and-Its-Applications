import numpy as np

A = np.array([[1, -1, 0, 0],[0, 1, -3, 0],[0, 0, 1, -3],[0, 0, 0, 2]]) # coefficient matrix
b = np.array([-4, -7, -1, 4])

solution = np.linalg.solve(A, b)
print(solution)