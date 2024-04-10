import cv2
import numpy as np
import csv
from skimage.measure import label, regionprops

for i in range(1,10000):
    # Load your frame (replace 'your_frame.jpg' with the actual file path)
    image = cv2.imread('frames/frame{}.jpg'.format(i),0)

    # rgb_frame = cv2.imread('ExpFrames/frame1.jpg')

    #image = cv2.bitwise_not(image)
    # Threshold the image to create a binary mask
    ret, binary_mask = cv2.threshold(image, 110, 255, cv2.THRESH_BINARY)
    binary_mask = cv2.bitwise_not(binary_mask)

    # Find contours in the binary mask
    contours, hierarchy = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a mask to fill holes

    filled_mask = np.zeros_like(binary_mask)

    # Fill each contour in the mask
    cv2.drawContours(filled_mask, contours, -1, 255, thickness=cv2.FILLED)
    output_path='btp/Thresholded_images/image_{}.png'.format(i)
    cv2.imwrite(output_path, filled_mask)
    print(f"Particles data for frame {i} has been saved to {output_path}.")

    
    # Binarize the frame using an appropriate thresholding method
    # _, binary_frame = cv2.threshold(graframe, 70, 255, cv2.THRESH_BINARY)

    # Label connected components in the binary image
    label_im = label(filled_mask)
    output_path='results/Labeled_images/labeled_image_{}.png'.format(i)
    cv2.imwrite(output_path, label_im)
    print(f"Particles data for frame {i} has been saved to {output_path}.")
