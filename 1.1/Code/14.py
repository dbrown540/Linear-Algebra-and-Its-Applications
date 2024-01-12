import numpy as np

A = np.array([[1, -3, 0],[-1, 1, 5],[0, 1, 1]])
b = np.array([5, 2, 0])

solution = np.linalg.solve(A, b)
print(solution)