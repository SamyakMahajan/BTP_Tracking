import cv2
import pandas as pd
import os
# 53731
for key in range(25000,30000):
    # os.mkdir('Cluster_CSVs/Cluster_{}'.format(key))

    Frame_dict = {}
    key_to_find = key
    first_frame_found=False
    print("processing for key",key)
    # Load the image
    for image_index in range(1000,10000):
        image_path = 'btp/Labeled_images/labeled_image_{}.png'.format(image_index)
        image = cv2.imread(image_path)

        centroid_df = pd.read_csv('btp/CSVs/cluster_data_frame{}.csv'.format(image_index))
        key_df = pd.read_csv('btp/Keys/Keys_{}.csv'.format(image_index))

        filtered_row = key_df[key_df['Key'] == key_to_find]
        
        if not filtered_row.empty:
            if( first_frame_found==False):
                first_frame_found=True
            label_value_in_this_frame = filtered_row['Id'].values[0]
            print(f"The value for the key {key_to_find} in frame {image_index} is: {label_value_in_this_frame}")
            ####THERE IS AN ERROR THAT NEEDS TO BE FIXED HERE!!!!! 
            # MAKE SURE TO WRITE CODE SUCH THAT IT DOESNT NEED THE FOLLOWING CONTINUE STATEMENT!!!
            # Assuming columns are 'Id', 'Centroid_x', 'Centroid_y', 'Area', 'Eccentricity' in centroid_df
            if(centroid_df[centroid_df['Id'] == label_value_in_this_frame].empty):
                continue
            Frame_dict[image_index] = centroid_df[centroid_df['Id'] == label_value_in_this_frame].iloc[0].to_dict()
            # print(centroid_df[centroid_df['Id'] == label_value_in_this_frame])
            # centroid_df[centroid_df['Id'] == label_value_in_this_frame].iloc[0].to_dict()
        elif first_frame_found:
            print(f"No entry found for the key {key_to_find} in frame {image_index}")
            break

    # Create a DataFrame from Frame_dict
    frame_df = pd.DataFrame.from_dict(Frame_dict, orient='index')
    # print(frame_df.shape[0])
    # if(frame_df.shape[0]<20):
    #     continue
    # Save the DataFrame to a CSV file
    output_csv_path = 'btp/Cluster_CSVs/keys_data_{}.csv'.format(key_to_find)  # Replace with the desired output path
    frame_df.to_csv(output_csv_path, index_label='Frame')

    print("CSV file created at:", output_csv_path)
