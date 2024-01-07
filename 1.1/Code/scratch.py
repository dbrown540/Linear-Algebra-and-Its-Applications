import plotly.graph_objects as go
import numpy as np

# Coefficient matrix A and constant vector B
A = np.array([
    [1, -1, 0, 0],
    [0, 1, -3, 0],
    [0, 0, 1, -3],
    [0, 0, 0, 1]
])

B = np.array([-4, -7, -1, -3])

# Solve for the variables x1, x2, x3, x4
x = np.linalg.solve(A[:, :4], B)

# Create a 3D scatter plot for x1, x2, x3 and use color for x4
fig = go.Figure(data=[
    go.Scatter3d(
        x=[x[0]],
        y=[x[1]],
        z=[x[2]],
        mode='markers',
        marker=dict(
            size=10,
            color=[x[3]],
            colorscale='Viridis',
            colorbar=dict(title='x4')
        )
    )
])

# Set axis labels
fig.update_layout(scene=dict(
    xaxis_title='x1',
    yaxis_title='x2',
    zaxis_title='x3'
))

# Show the plot
fig.show()
