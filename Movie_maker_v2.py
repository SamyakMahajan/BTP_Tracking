import cv2
import numpy as np
import os

def create_overlapping_movie(input_folder, output_path, fade_factor=0, fps=1):
    # Get a list of all image files in the folder
    image_files = [file for file in os.listdir(input_folder) if file.lower().endswith(('.jpg', '.jpeg', '.png'))]
    image_files.sort()  # Sort the files to ensure the correct order

    # Load the first image
    img1 = cv2.imread(os.path.join(input_folder, image_files[0]))

    # Get image dimensions
    height, width, _ = img1.shape

    # Define video writer with the specified fps
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Write the first frame to the video
    out.write(img1)

    # Loop through the remaining frames
    for i in range(1, len(image_files)):
        # Load the current frame
        img2 = cv2.imread(os.path.join(input_folder, image_files[i]))

        # Resize the current frame to match the dimensions of the first frame
        img2 = cv2.resize(img2, (width, height))

        # Adjust the brightness of the previous frame
        img1 = cv2.addWeighted(img1, fade_factor, np.zeros_like(img1), 0, 0)

        # Overlay the current frame on top of the faded previous frame
        result = cv2.addWeighted(img1, 1, img2, 1, 0)

        # Write the overlapped frame to the video
        out.write(result)

        # Update img1 for the next iteration
        img1 = result

    # Release the video writer
    out.release()

# Example usage with fps set to 1 frame per second
input_folder = 'BTP4/Centroids'
output_path = 'overlapping_movie_with_centroids_1fps_no_previouschrome'.avi'
create_overlapping_movie(input_folder, output_path, fps=1)
