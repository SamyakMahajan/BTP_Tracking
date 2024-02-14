import cv2
import os

# Folder containing frames
frames_folder = 'Cluster_70'

# Output video file
output_video_path = 'video_70_3fps.avi'

# Get a list of all image files in the folder
image_files = [f for f in os.listdir(frames_folder) if f.endswith(('.png'))]

# Sort the image files based on their names to maintain the correct order
image_files.sort()

# Get the first image to determine dimensions
first_image_path = os.path.join(frames_folder, image_files[0])
first_image = cv2.imread(first_image_path)
height, width, layers = first_image.shape

# Create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # You can use other codecs like MJPG or DIVX
video = cv2.VideoWriter(output_video_path, fourcc, 3, (width, height))

# Write each frame to the video
for image_file in image_files:
    image_path = os.path.join(frames_folder, image_file)
    frame = cv2.imread(image_path)
    video.write(frame)

# Release the video writer
video.release()

print(f"Video created at: {output_video_path}")
