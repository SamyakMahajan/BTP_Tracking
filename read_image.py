import cv2

# Load your RGB frame (replace 'your_frame.jpg' with the actual file path)
rgb_frame = cv2.imread('ExpFrames/frame1.jpg')

# Convert the RGB frame to grayscale
gray_frame = cv2.cvtColor(rgb_frame, cv2.COLOR_BGR2GRAY)

# Binarize the grayscale frame using an appropriate thresholding method
_, binary_frame = cv2.threshold(gray_frame, 50, 255, cv2.THRESH_BINARY)

# Display or further process the binary frame as needed
cv2.imshow('Binary Frame', binary_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
