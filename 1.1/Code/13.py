import numpy as np

A = np.array([[1, 0, -3],[2, 2, 9],[0, 1, 5]])
b = np.array([8, 7, -2])

solution = np.linalg.solve(A, b)
print(solution)