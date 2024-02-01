import cv2
import pandas as pd
import numpy as np

def overlay_red_dots(image_path, csv_file_path, output_path):
    # Read the original image
    image = cv2.imread(image_path)

    # Read center coordinates from the CSV file
    df = pd.read_csv(csv_file_path)
    center_coordinates = list(zip(df['Centroid_x'].astype(int), df['Centroid_y'].astype(int)))

    # Overlay red dots on the image
    for cx, cy in center_coordinates:
        # Draw a red dot on the image
        cv2.circle(image, (cx, cy), radius=3, color=(0, 0, 255), thickness=-1)  # -1 fills the circle

    # Save the image with overlaid red dots
    cv2.imwrite(output_path, image)

# Example usage
image_path = '../BTP4/Labeled_Images/labeled_image_1.png'
csv_file_path = '../BTP4/CSVs/particle_data_Img_2.csv'
output_path = 'centroids_of_Img_2_on_labeled_image_1.jpg'

overlay_red_dots(image_path, csv_file_path, output_path)
