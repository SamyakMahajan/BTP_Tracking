import cv2
import numpy as np
from skimage.measure import label, regionprops

for i in range(1,50):
    # Load your frame
    image = cv2.imread('frames/frame{}.jpg'.format(i), 0)

    # Threshold the image to create a binary mask
    ret, binary_mask = cv2.threshold(image, 110, 255, cv2.THRESH_BINARY)
    binary_mask = cv2.bitwise_not(binary_mask)

    # Find contours in the binary mask
    contours, hierarchy = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a mask to fill holes
    filled_mask = np.zeros_like(binary_mask)

    # Fill each contour in the mask
    cv2.drawContours(filled_mask, contours, -1, 255, thickness=cv2.FILLED)

    # Label connected components in the binary image
    label_im = label(filled_mask)

    # Get region properties for each labeled component
    regions = regionprops(label_im)

    # Initialize a list to store particle information
    particle_data = []

    # Define the area range you want to consider
    min_area = 100  # Replace with your desired minimum area
    max_area = 10000  # Replace with your desired maximum area

    # Loop through each labeled region (particle)
    for particle_id, props in enumerate(regions, start=1):
        # Extract properties
        particle_centroid = props.centroid  # (y, x) format
        particle_area = props.area

        if min_area <= particle_area <= max_area:
            # Store data in a dictionary
            particle_info = {
                'Id': particle_id,
                'Centroid_x': int(particle_centroid[1]),
                'Centroid_y': int(particle_centroid[0]),
                'Area': particle_area,
                'Eccentricity': props.eccentricity,
                'MajorAxisLength': props.minor_axis_length,
                'MinorAxisLength': props.major_axis_length,
                'Orientation': props.orientation
            }

            # Append the dictionary to the list
            particle_data.append(particle_info)

    # Draw ellipses around detected particles
    image_with_ellipses = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)  # Convert image to color for drawing
    for particle in particle_data:
        center = (particle['Centroid_x'], particle['Centroid_y'])
        axes = (int(particle['MajorAxisLength'] / 2), int(particle['MinorAxisLength'] / 2))
        angle = np.degrees(-particle['Orientation'])  # Negative orientation to match OpenCV's convention
        cv2.ellipse(image_with_ellipses, center, axes, angle, 0, 360, (0, 255, 0), 2)  # Draw ellipse

    # Display or save the image with ellipses
    # cv2.imshow('Image with Ellipses', image_with_ellipses)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    output_path='results/ellipses_on_image/image_{}.png'.format(i)
    cv2.imwrite(output_path, image_with_ellipses)
    
