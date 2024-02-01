import cv2
import numpy as np

# Read the image
image = cv2.imread('BTP_IMGS3/Img (88).png', 0)  # Read as grayscale
image = cv2.bitwise_not(image)
# Threshold the image to create a binary mask
ret, binary_mask = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)
binary_mask = cv2.bitwise_not(binary_mask)

# Find contours in the binary mask
contours, hierarchy = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a mask to fill holes

filled_mask = np.zeros_like(binary_mask)

# Fill each contour in the mask
cv2.drawContours(filled_mask, contours, -1, 255, thickness=cv2.FILLED)
# kernel = np.ones((5, 5), np.uint8)  # Adjust the kernel size as needed
# erosion = cv2.erode(filled_mask, kernel, iterations=1)

# cv2.imwrite("image_err.jpg", erosion)
# filled_mask=erosion

# Perform connected component analysis
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(filled_mask, connectivity=8)

# Create a mask for all connected components
all_components_mask = (labels > 0).astype(np.uint8) * 255
# all_components_mask = (stats[]).astype(np.uint8) * 255

# Overlay the mask on the original image
result_image = cv2.bitwise_and(image, image, mask=all_components_mask)

# Create a pixel map where each pixel value represents the component it belongs to
pixel_map = labels.copy().astype(np.uint8)
pixel_map[pixel_map > 0] += 1  # Increment component values to start from 1 (excluding background)

# Define a function to modify pixel values
def modify_pixel_value(value):
    # Example: square the values
    col=(7191*value)%(170)+70 
    
    
        # col+=50

    return col

for i in range(len(pixel_map)):
    for j in range(len(pixel_map[i])):
        pixel_map[i][j]=modify_pixel_value(pixel_map[i][j])


# Apply the function to each pixel value in the pixel map
# modified_pixel_map = np.vectorize(modify_pixel_value)(pixel_map)

# Display the modified pixel map
cv2.imshow('Modified Connected Components Pixel Map', pixel_map)
cv2.imwrite("Modified_CCA_pixel_map500.jpg", pixel_map)

cv2.waitKey(0)
cv2.destroyAllWindows()
