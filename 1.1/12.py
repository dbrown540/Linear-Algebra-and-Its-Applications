import numpy as np

A = np.array([[1, -3, 4], [3, -7, 7], [-4, 6, -1]]) #coefficients
b = np.array([-4, -8, 7])

solution = np.linalg.solve(A, b)

print(solution)

# Error means it is either inconsistent or has infinite many solutions