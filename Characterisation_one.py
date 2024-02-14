import cv2
import numpy as np
import csv
from skimage.measure import label, regionprops

i = 1
# Load your frame (replace 'ExpFrames/frame{}.jpg' with the actual file path)
image = cv2.imread('ExpFrames/frame{}.jpg'.format(i), 0)

# Threshold the image to create a binary mask
ret, binary_mask = cv2.threshold(image, 110, 255, cv2.THRESH_BINARY)
binary_mask = cv2.bitwise_not(binary_mask)

# Find contours in the binary mask
contours, hierarchy = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a mask to fill holes
filled_mask = np.zeros_like(binary_mask)

# Fill each contour in the mask
cv2.drawContours(filled_mask, contours, -1, 255, thickness=cv2.FILLED)

# Label connected components in the binary image
label_im = label(filled_mask)

# print(type(label_im))
# Get region properties for each labeled component
regions = regionprops(label_im)
print(regions[0].label)
# Initialize a list to store particle information
particle_data = []

# Define the area range you want to consider
min_area = 100  # Replace with your desired minimum area
max_area = 10000  # Replace with your desired maximum area

# Loop through each labeled region (particle)
for particle_id, props in enumerate(regions, start=1):
    # Extract properties
    particle_centroid = props.centroid  # (y, x) format
    particle_area = props.area

    # Check if the area is within the specified range
    if min_area <= particle_area <= max_area:
        # Store data in a dictionary
        particle_info = {
            'Id': particle_id,
            'Centroid_x': int(particle_centroid[1]),
            'Centroid_y': int(particle_centroid[0]),
            'Area': particle_area
        }

        # Append the dictionary to the list
        particle_data.append(particle_info)

# Save the particle data to a CSV file
csv_file_path = '_particle_data_Img_1_filtered.csv'
with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = ['Id', 'Centroid_x', 'Centroid_y', 'Area']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the data
    writer.writerows(particle_data)

print(f"Particle data for clusters with area in the range [{min_area}, {max_area}] has been saved to {csv_file_path}.")
