import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Define the size of the grid
grid_size = 100

# Generate initial x and y values for each pixel
x_values = np.random.uniform(-1, 1, size=(grid_size, grid_size))
y_values = np.random.uniform(-1, 1, size=(grid_size, grid_size))

print(x_values)


# Define the function to update the values of each pixel over time
def update(frame):
    global x_values, y_values  # Declare x_values and y_values as global variables
    # Implement your calculation here to update the x_values and y_values arrays
    # For demonstration purposes, let's just add a small amount to each value
    x_values += 0.1
    y_values += 0.1


    
    return plt.imshow(np.sin(x_values) * np.cos(y_values), cmap='viridis', extent=[-1, 1, -1, 1])

# Create the initial plot
fig, ax = plt.subplots()
im = ax.imshow(np.sin(x_values) * np.cos(y_values), cmap='viridis', extent=[-1, 1, -1, 1])
plt.colorbar(im, ax=ax, label='Value')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Animation of Pixel Values')

# Create the animation
ani = FuncAnimation(fig, update, frames=range(1000000), interval=0)

plt.show()
