import numpy as np
import matplotlib.pyplot as plt

# Define coefficients for each linear equation

a1, b1, c1, d1 = 1, -4, 9, 0
a2, b2, c2, d2 = 0, 1, 7, 0
a3, b3, c3, d3 = 0, 0, 2, 0

# Create a range of x and y values to plot from then create a meshgrid

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

xx, yy = np.meshgrid(x, y)

# Create equations for planes  ->  ax + by + cz = d  ->  z = (d - ax - by)/c

z1 = (d1 - a1 * xx - b1 * yy)/c1
z2 = (d2 - a2 * xx - b2 * yy)/c2
z3 = (d3 - a3 * xx - b2 * yy)/c3

# Create a figure and a space to add the planes to

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

# Add the surfaces to the subplot

ax.plot_surface(xx, yy, z1, alpha = 0.5, color='b')
ax.plot_surface(xx, yy, z2, alpha = 0.5, color ='g')
ax.plot_surface(xx, yy, z3, alpha = 0.5, color='r')

# Change viewing angle of the figure 

ax.view_init(elev=20, azim=30)  # Adjust elev and azim as needed

# Analytically solve the system of equations
A = np.array([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])  # Coefficients
b = np.array([d1, d2, d3])  # Augmented
intersection = np.linalg.solve(A, b)

# Create symbols for the planes to be used for the legend
legend1_symbol = plt.Line2D([0], [0], linestyle="none", c='b', marker='o')
legend2_symbol = plt.Line2D([0], [0], linestyle="none", c='r', marker='o')
legend3_symbol = plt.Line2D([0], [0], linestyle="none", c='g', marker='o')

# Create the intersection point (solution)
intersection_point = ax.scatter(*intersection, color='purple', label='Intersection Point')

# Create legend
ax.legend([legend1_symbol, legend2_symbol, legend3_symbol, intersection_point],['Plane 1', 'Plane 2', 'Plane 3', 'Intersection point'], loc='upper right')

# Create title and axes
ax.set_title('Exercise 8')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Show the plot
plt.show()