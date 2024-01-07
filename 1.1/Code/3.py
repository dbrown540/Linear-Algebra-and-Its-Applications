import numpy as np
import matplotlib.pyplot as plt

# Define the system of equations:
# Let x1 be the x-axis and x2 be the y-axis

def equation1(x1): # f(x1) = x2
    return(7/5 - x1/7)

def equation2(x1):
    return(x1/2 + 1)

# Define x-bounds

x1_values = np.linspace(-5, 7, 100)

# Generate x2 values

x2_values_eq1 = equation1(x1_values)
x2_values_eq2 = equation2(x1_values)

# Solve the system of equations computationally:

A = np.array([[1, 5], [1, -2]]) # Coefficient
b = np.array([7, -2]) # Augmented part

intersection = np.linalg.solve(A,b)
print(intersection)

# Plot the equations

plt.plot(x1_values, x2_values_eq1, label=r'$x_1 + 5x_2 = 7$', color='#21C4F0')
plt.plot(x1_values, x2_values_eq2, label=r'$x_1 - 2x_2 = -2$', color='#21C4F0')

# Set labels and and title

plt.title('Plot 1: Systems of Equations for Exercise 3')
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.axhline(0, color='black', linewidth='0.5')
plt.axvline(0, color='black', linewidth='0.5')
plt.legend()
plt.show()
