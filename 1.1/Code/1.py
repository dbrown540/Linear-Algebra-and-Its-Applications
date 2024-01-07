import numpy as np
import matplotlib.pyplot as plt

# Create the coefficient matrix and constant vector

A = np.array([[1, 5], [-2, -7]])  # Coefficient matrix
b = np.array([7, -5])             # Constant vector

# Solve the system of equations computationally

solution = np.linalg.solve(A, b)
print("Solution:", solution)  # [-8, 3]

# Plot the systems of equations

# Create a range of x_1 values
x = np.linspace(-10, 10, 500)

# Make equations
equation1 = (7 - x) / 5
equation2 = (2 * x - 5) / (-7)

# Plot equations
plt.plot(x, equation1, label='Eq 1')
plt.plot(x, equation2, label='Eq 2')

plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.title('Exercise 1')
plt.axhline(0, color='black', linewidth=0.5)  # Horizontal line at y=0
plt.axvline(0, color='black', linewidth=0.5)  # Vertical line at x=0

# Plot intersection point
plt.scatter(*solution, color='green', label='Solution')

# Create legend
plt.legend()

plt.show()
