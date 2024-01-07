import numpy as np

A = np.array([[1, -2, 0, 3],[0, 1, 0, -4],[0, 0, 1, 0],[0, 0, 0, 1]]) #coefficient matrix
b = np.array([-2, 7, 6, -3])

solution = np.linalg.solve(A,b)

print(solution)