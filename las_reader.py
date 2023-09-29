import laspy
from scipy.spatial import cKDTree
import numpy as np
import matplotlib.pyplot as plt

las = laspy.read("new_file.las")
# Grab a numpy dataset of our clustering dimensions:
dataset = np.vstack((las.X, las.Y, las.Z)).transpose()
# Build the KD Tree
tree = cKDTree(dataset)
# This should do the same as the FLANN example above, though it might
# be a little slower.
neighbors_distance, neighbors_indices = tree.query(dataset[100], k=5)
print(neighbors_indices)
print(neighbors_distance)

ground_points = las.points[las.number_of_returns == las.return_number]

print("%i points out of %i were ground points." % (len(ground_points),
        len(las.points)))

        
plt.hist(las.intensity)
plt.title("Histogram of the Intensity Dimension")
plt.savefig('graph.png')

x = las.X
y = las.Y
z = las.Z

plt.figure(figsize=(10, 6))
plt.scatter(x, y, s=1, c=z, cmap='viridis', alpha=0.5)
plt.colorbar(label='Z')
plt.title("Scatter Plot of LiDAR Points")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")

# Set axis limits based on the data range
plt.xlim(min(x), max(x))
plt.ylim(min(y), max(y))

# Save the scatter plot as an image
plt.savefig('scatter_plot.png')