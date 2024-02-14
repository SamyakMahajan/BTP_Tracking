import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the image
for i in range(61):
    image_path = '../../BTP4/Labeled_Images/labeled_image_{}.png'.format(i)
    image = cv2.imread(image_path)

    centroid_df=pd.read_csv('../../BTP4/CSVs/particle_data_Img_{}.csv'.format(i))
    key_df=pd.read_csv('../../BTP4/Keys/Keys_{}.csv'.format(i))
    
    key_to_find=70
    filtered_row = key_df[key_df['Key'] == 70]
    if not filtered_row.empty:
        label_value = filtered_row['Id'].values[0]
        print(f"The value for the key {key_to_find} in frame {i} is: {label_value}")
    else:
        print(f"No entry found for the key {key_to_find} in frame {i}")
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Find pixels with brightness 70
    brightness_value = label_value
    pixels_with_brightness_70 = (gray_image == brightness_value)

    
    # Create an output image with only pixels having brightness 70 set to red
    result = image.copy()
    result[pixels_with_brightness_70] = [0, 0, 255]  # Set pixels to red (BGR format)

    # Save the final image
    output_image_path = 'Cluster_70/result_image_{}.png'.format(i)  # Replace with the desired output path
    cv2.imwrite(output_image_path, result)

    # plt.show()