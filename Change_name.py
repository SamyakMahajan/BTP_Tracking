import os
from datetime import datetime

# Specify the directory containing the images
image_directory = 'BTP_IMGS3'

# Change the current working directory to the image directory
os.chdir(image_directory)

# Get a list of all image files in the directory
image_files = [file for file in os.listdir() if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]

# Sort the image files based on their timestamps
image_files.sort(key=lambda x: os.path.getmtime(x))

# Rename the images
for i, old_name in enumerate(image_files):
    timestamp = datetime.fromtimestamp(os.path.getmtime(old_name)).strftime('%Y%m%d%H%M%S')
    new_name = f'Image_{i + 1}.jpg'  # Change the extension accordingly
    os.rename(old_name, new_name)

print("Images have been renamed successfully.")
