import cv2
import numpy as np
import csv
from skimage.measure import label, regionprops

for i in range(62):
    # Load your frame (replace 'your_frame.jpg' with the actual file path)
    frame = cv2.imread('BTP4/Img_{}.png'.format(i), cv2.IMREAD_GRAYSCALE)

    # Binarize the frame using an appropriate thresholding method
    _, binary_frame = cv2.threshold(frame, 128, 255, cv2.THRESH_BINARY)

    # Label connected components in the binary image
    label_im = label(binary_frame)
    output_path='BTP4/Labeled_Images/labeled_image_{}.png'.format(i)
    cv2.imwrite(output_path, label_im)
    print(f"Particles data for frame {i} has been saved to {output_path}.")
