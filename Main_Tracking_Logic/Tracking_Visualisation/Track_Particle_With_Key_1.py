import cv2
import numpy as np

# Load the image
image = cv2.imread('your_image_path.jpg')  # Replace 'your_image_path.jpg' with the path to your image

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold the image to get a binary mask where pixels with brightness 70 are white
ret, binary_mask = cv2.threshold(gray_image, 70, 255, cv2.THRESH_BINARY)

# Apply the binary mask to the original image
result = cv2.bitwise_and(image, image, mask=binary_mask)

# Display the original image, grayscale image, binary mask, and the result
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('Binary Mask', binary_mask)
cv2.imshow('Result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
