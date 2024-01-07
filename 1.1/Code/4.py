import numpy as np
import matplotlib.pyplot as plt

def equation1(x1): # f(x1) = x2
    return((x1-1)/5)

def equation2(x1): # f(x1) = x2
    return((3*x1 - 5)/7)

# Define x bounds

x1_values = np.linspace(-3, 5, 100)

# Create arrays of x2 solutions

x2_equation1 = equation1(x1_values)
x2_equation2 = equation2(x1_values)

# Plot the arrays

plt.plot(x1_values, x2_equation1, label=r'$x_1 - 5x_2 = 1$', color='#21C4F0')
plt.plot(x1_values, x2_equation2, label=r'$3x_1 - 7x_2 = 5$', color='#21C4F0')
plt.axhline(0, color='black', linewidth='0.5')
plt.axvline(0, color='black', linewidth='0.5')
plt.legend()
plt.show()

# Solve the system of equations computationally

A = np.array([[1, -5], [3, -7]]) # Coefficients
b = np.array([1, 5]) # Augmented

intersection = np.linalg.solve(A,b)
print(intersection)