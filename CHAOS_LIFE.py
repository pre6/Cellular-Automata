import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

grid_size = 100

# Generate initial x and y values for each pixel
x_values = np.random.uniform(-1, 1, size=(grid_size, grid_size))
y_values = np.random.uniform(-1, 1, size=(grid_size, grid_size))

print(x_values[50,60])

def chaotic_update(frame):
    global x_values, y_values, N, r
    
    # Logistic map parameters
    r = 2  # Control parameter for the logistic map
    
    # Define logistic map function
    logistic_map = lambda x, r: r * x * (1 - x)
    

    # Update x_values and y_values arrays using the logistic map
    x_values = logistic_map(x_values, r)
    y_values = logistic_map(y_values, r)
    
    return plt.imshow(np.sin(x_values) * np.cos(y_values), cmap='viridis', extent=[-1, 1, -1, 1])


# # Define the function to update the values of each pixel over time
# def update(frame):
#     global x_values, y_values , N # Declare x_values and y_values as global variables
#     # Implement your calculation here to update the x_values and y_values arrays
#     # For demonstration purposes, let's just add a small amount to each value
    
#     # print(x_values[50,60])
#     N= 100
#     newGrid_x = x_values.copy() 
	
#     for i in range(grid_size): 
#         for j in range(grid_size): 

#             # compute 8-neighbor sum 
#             # using toroidal boundary conditions - x and y wrap around 
#             # so that the simulation takes place on a toroidal surface. 
#             total = ((x_values[i, (j-1)%N] + x_values[i, (j+1)%N] +
#                         x_values[(i-1)%N, j] + x_values[(i+1)%N, j] +
#                         x_values[(i-1)%N, (j-1)%N] + x_values[(i-1)%N, (j+1)%N] +
#                         x_values[(i+1)%N, (j-1)%N] + x_values[(i+1)%N, (j+1)%N])) 
#             # print(total)
#             # apply Conway's rules 
#             if x_values[i, j] > 0: 
#                 if (total < -0.5) or (total > -0.25): 
#                     newGrid_x[i, j] = -1
#                 else:
#                     newGrid_x[i, j] += 0.25
#             else: 
#                 if total == -0.25: 
#                     newGrid_x[i, j] = 0.25
#                 elif total < -0.25:
#                     newGrid_x[i, j] += 0.025
            
#             if x_values[i, j] > 0.5:
#                 newGrid_x[i, j] += -0.5



#     newGrid_y = y_values.copy() 
	
#     for i in range(grid_size): 
#         for j in range(grid_size): 

#             # compute 8-neighbor sum 
#             # using toroidal boundary conditions - x and y wrap around 
#             # so that the simulation takes place on a toroidal surface. 
#             total = ((y_values[i, (j-1)%N] + y_values[i, (j+1)%N] +
#                         y_values[(i-1)%N, j] + y_values[(i+1)%N, j] +
#                         y_values[(i-1)%N, (j-1)%N] + y_values[(i-1)%N, (j+1)%N] +
#                         y_values[(i+1)%N, (j-1)%N] + y_values[(i+1)%N, (j+1)%N])/255) 

#             # apply Conway's rules 
#             if y_values[i, j] > 0: 
#                 if (total < -0.5) or (total > -0.25): 
#                     newGrid_y[i, j] = -1
#                 else:
#                     newGrid_y[i, j] += 0.25
#             else: 
#                 if total == -0.25: 
#                     newGrid_y[i, j] = 0.25
#                 elif total < -0.25:
#                     newGrid_y[i, j] += 0.025

#             if y_values[i, j] > 0.5:
#                 newGrid_y[i, j] += -0.5


    
    
#     x_values = newGrid_x 
#     y_values = newGrid_y


    
#     return plt.imshow(np.sin(x_values) * np.cos(y_values), cmap='viridis', extent=[-1, 1, -1, 1])



# Create the initial plot
fig, ax = plt.subplots()
im = ax.imshow(np.sin(x_values) * np.cos(y_values), cmap='viridis', extent=[-1, 1, -1, 1])
plt.colorbar(im, ax=ax, label='Value')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Animation of Pixel Values')

# Create the animation
ani = FuncAnimation(fig, chaotic_update, frames=range(1000000), interval=0)

plt.show()