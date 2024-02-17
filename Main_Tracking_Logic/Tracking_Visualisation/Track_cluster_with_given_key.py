import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

for key in range(1,70):
    try:
        os.mkdir('Cluster_Tracks/Exp_Cluster_{}'.format(key))
    except:
        pass
    key_to_find=key
    # Load the image
    for i in range(1,50):
        image_path = '../../ExpFrames/Labeled_images/labeled_image_{}.png'.format(i)
        image = cv2.imread(image_path)

        centroid_df=pd.read_csv('../../ExpFrames/CSVs/cluster_data_frame{}.csv'.format(i))
        key_df=pd.read_csv('../../ExpFrames/Keys/Keys_{}.csv'.format(i))
        
        
        filtered_row = key_df[key_df['Key'] == key_to_find]
        if not filtered_row.empty:
            label_value = filtered_row['Id'].values[0]
            print(f"The Id for the key {key_to_find} in frame {i} is: {label_value}")
        else:
            print(f"No entry found for the key {key_to_find} in frame {i}")
            break
        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Find pixels with brightness 70
        brightness_value = label_value
        pixels_with_brightness_70 = (gray_image == brightness_value)

        
        # Create an output image with only pixels having brightness 70 set to red
        result = image.copy()
        result[pixels_with_brightness_70] = [0, 0, 255]  # Set pixels to red (BGR format)

        # Save the final image
        
        output_image_path = 'Cluster_Tracks/Exp_Cluster_{}/result_frame_{}.png'.format(key_to_find,i)  # Replace with the desired output path
        cv2.imwrite(output_image_path, result)

        # plt.show()
