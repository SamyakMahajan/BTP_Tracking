import cv2
import numpy as np

# Load the first image
img1 = cv2.imread('BTP4/Img_0.png', cv2.IMREAD_GRAYSCALE)

# Load the second image
img2 = cv2.imread('BTP4/Img_4.png', cv2.IMREAD_GRAYSCALE)

# Resize the second image to match the dimensions of the first image
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Adjust the brightness of the first image
img1 = cv2.addWeighted(img1, 0.8, np.zeros_like(img1), 0, 0)

# Overlay the second image on top of the first one
result = cv2.addWeighted(img1, 1, img2, 1, 0)

cv2.imwrite("overlapped.jpg", result)

# # Display the result
# cv2.imshow('Overlayed Image', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
