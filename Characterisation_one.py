import cv2
import numpy as np
import csv
from skimage.measure import label, regionprops

# Load your frame (replace 'your_frame.jpg' with the actual file path)
frame = cv2.imread('BTP4/Img_1.png', cv2.IMREAD_GRAYSCALE)

# Binarize the frame using an appropriate thresholding method
_, binary_frame = cv2.threshold(frame, 128, 255, cv2.THRESH_BINARY)

# Label connected components in the binary image
label_im = label(binary_frame)

# Get region properties for each labeled component
regions = regionprops(label_im)

# Initialize a list to store particle information
particle_data = []

# Loop through each labeled region (particle)
for particle_id, props in enumerate(regions, start=1):
    # Extract properties
    particle_centroid = props.centroid  # (y, x) format
    particle_area = props.area

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
csv_file_path = 'particle_data_Img_1.csv'
with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = ['Id', 'Centroid_x', 'Centroid_y', 'Area']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the data
    writer.writerows(particle_data)

print(f"Particle data has been saved to {csv_file_path}.")
