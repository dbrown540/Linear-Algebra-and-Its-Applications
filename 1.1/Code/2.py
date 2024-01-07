import numpy as np
import matplotlib.pyplot as plt

# Define x values for the plot
x = np.linspace(0, 15, 100)

# Equations for lines
equation1 = (-4 - 2 * x) / 4
equation2 = (11 - 5 * x) / 7

# Create the coefficient matrix and constant vector for the system of linear equations
A = np.array([[2, 4], [5, 7]])  # Coefficient matrix
b = np.array([-4, 11])          # Constant vector

# Solve the system of linear equations to find the intersection point
solution = np.linalg.solve(A, b)
print("Intersection point:", solution)

# Plot the intersection point
plt.scatter(*solution, color='red', label=f'Solution ({round(solution[0])}, {round(solution[1])})')

# Create the plot for the lines
plt.plot(x, equation1, label=r'$x_1$')
plt.plot(x, equation2, label=r'$x_2$')

# Set labels and add gridlines
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Add legend and display the plot
plt.legend()
plt.show()
