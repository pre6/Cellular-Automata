import numpy as np
import matplotlib.pyplot as plt

# Define grid size
grid_size = 10

# Generate random values for x and y within the range (-1, 1)
x_values = np.random.uniform(-1, 1, size=(grid_size, grid_size))
y_values = np.random.uniform(-1, 1, size=(grid_size, grid_size))

# Generate random colors within a specified range
colors = np.random.uniform(0, 1, size=(grid_size, grid_size))

# Plot using matplotlib
plt.scatter(x_values, y_values, c=colors, cmap='coolwarm')
plt.colorbar()
plt.show()
