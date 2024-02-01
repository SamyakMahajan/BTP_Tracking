import cv2
import numpy as np

# Read the image
image = cv2.imread('frame36000.jpg', 0)  # Read as grayscale

# Threshold the image to create a binary mask
ret, binary_mask = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)
binary_mask = cv2.bitwise_not(binary_mask)

# Find contours in the binary mask
contours, hierarchy = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a mask to fill holes
filled_mask = np.zeros_like(binary_mask)

# Fill each contour in the mask
cv2.drawContours(filled_mask, contours, -1, 255, thickness=cv2.FILLED)
kernel = np.ones((2, 2), np.uint8)  # Adjust the kernel size as needed

erosion = cv2.erode(filled_mask, kernel, iterations=1)
image_filled=erosion
##cv2.imwrite("image_filled.jpg", filled_mask)

# Perform connected component analysis
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(filled_mask, connectivity=8)

# Create a mask for all connected components
all_components_mask = (labels > 0).astype(np.uint8) * 255

# Overlay the mask on the original image
result_image = cv2.bitwise_and(image, image, mask=all_components_mask)

# Create a pixel map where each pixel value represents the component it belongs to
pixel_map = labels.copy().astype(np.uint8)
pixel_map[pixel_map > 0] += 1  # Increment component values to start from 1 (excluding background)

# Read coordinates from the text file
# with open('frame36000.txt', 'r') as file:
#     coordinates = [tuple(map(float, line.strip().split())) for line in file]

# Assign each coordinate to a connected component
# # Display the pixel map
cv2.imshow('Connected Components Pixel Map', pixel_map)
cv2.imwrite("CCA_pixel_map.jpg", pixel_map)
cv2.waitKey(0)

# # Print the number of clusters for each size
##import matplotlib.pyplot as plt;
##plt.plot([i for i in range(1,50)],cluster_sizes)
##plt.show()
for i in range(1,50):
 print(f'Number of clusters with size {i-1}: {cluster_sizes[i-1]}')
 k+=cluster_sizes[i-1]*(i-1)
print(k)
##import plotly.express as px
##
### Sample data
### x_data = [1, 2, 3, 4, 5]
### y_data = [2, 4, 1, 7, 3]
##
### Create a scatter plot
##fig = px.scatter(x=[i for i in range(1,50)], y=cluster_sizes, title='Simple Scatter Plot', labels={'x': 'X-axis', 'y': 'Y-axis'})
##
### Show the plot
##fig.show()
cv2.destroyAllWindows()
