# Python code to implement Conway's Game Of Life 

import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation 

# setting up the values for the grid 
ON = 255
OFF = 0
vals = [ON, OFF] 

def randomGrid(N): 

	"""returns a grid of NxN random values"""
	return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N) 




def update(frameNum, img, grid, N): 

	# copy grid since we require 8 neighbors 
	# for calculation and we go line by line 
	newGrid = grid.copy() 
	for i in range(N): 
		for j in range(N): 

			# compute 8-neighbor sum 
			# using toroidal boundary conditions - x and y wrap around 
			# so that the simulation takes place on a toroidal surface. 
			total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
						grid[(i-1)%N, j] + grid[(i+1)%N, j] +
						grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
						grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255) 
			if total >3:
				total += 3
			if grid[i, j] == ON: 
				if (total < 2) or (total > 3): 
					newGrid[i, j] = OFF 
			else: 
				if total == 3: 
					newGrid[i, j] = ON 

	# update data 
	img.set_data(newGrid) 
	grid[:] = newGrid[:] 
	return img, 

# main() function 
def main(): 




	
	# set grid size 
	N = 100

		
	# set animation update interval 
	updateInterval = 50


	# declare grid 
	grid = np.array([]) 


	grid = randomGrid(N) 

	# set up animation 
	fig, ax = plt.subplots() 
	img = ax.imshow(grid, interpolation='nearest') 
	ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ), 
								frames = 10, 
								interval=updateInterval) 



	plt.show() 

# call main 
if __name__ == '__main__': 
	main() 
