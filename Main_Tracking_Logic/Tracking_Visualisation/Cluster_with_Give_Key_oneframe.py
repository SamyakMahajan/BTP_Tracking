import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image
image_path = '../../BTP4/Labeled_Images/labeled_image_0.png'
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find pixels with brightness 70
brightness_value = 70
pixels_with_brightness_70 = (gray_image == brightness_value)

# Create an output image with only pixels having brightness 70 set to red
result = image.copy()
result[pixels_with_brightness_70] = [0, 0, 255]  # Set pixels to red (BGR format)

# Display the original image, grayscale image, and the result using Matplotlib
plt.figure(figsize=(10, 8))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(1, 3, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title('Pixels with Brightness 70 in Red')

plt.show()
