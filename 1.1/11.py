import numpy as np

A = np.array([[0, 1, 4], [1, 3, 5], [3, 7, 7]])
b = np.array([-5, -2, 6])

solution = np.linalg.solve(A, b)
print(solution)