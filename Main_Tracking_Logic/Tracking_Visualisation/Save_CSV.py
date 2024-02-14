import cv2
import pandas as pd
import os

for key in range(1,2):
    # os.mkdir('Cluster_CSVs/Cluster_{}'.format(key))

    Frame_dict = {}
    key_to_find = key
        
    # Load the image
    for image_index in range(1,50):
        image_path = '../../ExpFrames/Labeled_images/labeled_image_{}.png'.format(image_index)
        image = cv2.imread(image_path)

        centroid_df = pd.read_csv('../../ExpFrames/CSVs/cluster_data_frame{}.csv'.format(image_index))
        key_df = pd.read_csv('../../ExpFrames/Keys/Keys_{}.csv'.format(image_index))

        filtered_row = key_df[key_df['Key'] == key_to_find]
        
        if not filtered_row.empty:
            label_value = filtered_row['Id'].values[0]
            print(f"The value for the key {key_to_find} in frame {image_index} is: {label_value}")
            
            # Assuming columns are 'Id', 'Centroid_x', 'Centroid_y', 'Area', 'Eccentricity' in centroid_df
            Frame_dict[image_index] = centroid_df[centroid_df['Id'] == label_value].iloc[0].to_dict()
        else:
            print(f"No entry found for the key {key_to_find} in frame {image_index}")
            break

    # Create a DataFrame from Frame_dict
    frame_df = pd.DataFrame.from_dict(Frame_dict, orient='index')

    # Save the DataFrame to a CSV file
    output_csv_path = 'ExpFrames/Cluster_CSVs/keys_data_{}.csv'.format(key_to_find)  # Replace with the desired output path
    frame_df.to_csv(output_csv_path, index_label='Frame')

    print("CSV file created at:", output_csv_path)
