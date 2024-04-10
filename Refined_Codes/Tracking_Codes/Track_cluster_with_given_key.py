import cv2
import os
import pandas as pd

try:
    os.mkdir('Tracks')
except:
    pass

for key in range(100, 200):
    df = pd.read_csv('../btp/Cluster_CSVs/keys_data_{}.csv'.format(key))
    # Plot the trajectory
    if(df.shape[0]<100):
        print("Key",key,"'s life is too short to analyse")
        continue
    first_frame_found=False
    # print(df.iloc[0][0])
    try:
        os.mkdir('Tracks/Cluster_{}'.format(key))
    except:
        pass
    key_to_find = key

    for i in range(int(df.iloc[0][0]), 10000):
        image_path = '../btp/Labeled_images/labeled_image_{}.png'.format(i)
        image = cv2.imread(image_path)

        centroid_df = pd.read_csv('../btp/CSVs/cluster_data_frame{}.csv'.format(i))
        key_df = pd.read_csv('../btp/Keys/Keys_{}.csv'.format(i))

        filtered_row = key_df[key_df['Key'] == key_to_find]
        if not filtered_row.empty:
            if( first_frame_found==False):
                first_frame_found=True
            
            label_value = filtered_row['Id'].values[0]
            print(f"The Id for the key {key_to_find} in frame {i} is: {label_value}")
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            brightness_value = label_value
            pixels_with_brightness_70 = (gray_image == brightness_value)

            result = image.copy()
            result[pixels_with_brightness_70] = [0, 0, 255]

            output_image_path = 'Tracks/Cluster_{}/result_frame_{}.jpg'.format(key_to_find, i)
            cv2.imwrite(output_image_path, result, [cv2.IMWRITE_JPEG_QUALITY, 100])

        elif first_frame_found:
            print(f"No entry found for the key {key_to_find} in frame {i}")
            for k in range(i,i+10):
                image_path = '../btp/Labeled_images/labeled_image_{}.png'.format(k)
                image = cv2.imread(image_path)

                output_image_path = 'Tracks/Cluster_{}/result_frame_{}.jpg'.format(key_to_find, k)
                cv2.imwrite(output_image_path, image, [cv2.IMWRITE_JPEG_QUALITY, 25])

            break

        