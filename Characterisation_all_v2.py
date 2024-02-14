import cv2
import numpy as np
import csv
from skimage.measure import label, regionprops

for i in range(1,51):
    # Load your frame (replace 'your_frame.jpg' with the actual file path)
    image = cv2.imread('ExpFrames/frame{}.jpg'.format(i),0)

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

    # Binarize the frame using an appropriate thresholding method
    # _, binary_frame = cv2.threshold(graframe, 70, 255, cv2.THRESH_BINARY)

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
                'Eccentricity':props.eccentricity
            }
            """_summary_
                    __class__ : <class 'skimage.measure._regionprops.RegionProperties'>
                __delattr__ : <method-wrapper '__delattr__' of RegionProperties object at 0x7fb7c9347d60>
                __dict__ : {'label': 1, '_offset': array([0, 0]), '_slice': (slice(0, 38, None), slice(0, 28, None)), 'slice': (slice(0, 38, None), slice(0, 28, None)), '_label_image': array([[  1,   1,   1, ...,   0,   0,   0],
                    [  1,   1,   1, ...,   0,   0,   0],
                    [  1,   1,   1, ...,   0,   0,   0],
                    ...,
                    [  0,   0,   0, ..., 181, 181, 181],
                    [  0,   0,   0, ..., 181, 181, 181],
                    [  0,   0,   0, ..., 181, 181, 181]]), '_intensity_image': None, '_cache_active': True, '_cache': {}, '_ndim': 2, '_multichannel': False, '_spatial_axes': (0, 1), '_spacing': array([1., 1.]), '_pixel_area': 1.0, '_extra_properties': {}}
                __dir__ : <built-in method __dir__ of RegionProperties object at 0x7fb7c9347d60>
                __doc__ : Please refer to `skimage.measure.regionprops` for more information
                    on the available region properties.
                    
                __eq__ : <bound method RegionProperties.__eq__ of <skimage.measure._regionprops.RegionProperties object at 0x7fb7c9347d60>>
                __format__ : <built-in method __format__ of RegionProperties object at 0x7fb7c9347d60>
                __ge__ : <method-wrapper '__ge__' of RegionProperties object at 0x7fb7c9347d60>
                __getattr__ : <bound method RegionProperties.__getattr__ of <skimage.measure._regionprops.RegionProperties object at 0x7fb7c9347d60>>
                __getattribute__ : <method-wrapper '__getattribute__' of RegionProperties object at 0x7fb7c9347d60>
                __getitem__ : <bound method RegionProperties.__getitem__ of <skimage.measure._regionprops.RegionProperties object at 0x7fb7c9347d60>>
                __gt__ : <method-wrapper '__gt__' of RegionProperties object at 0x7fb7c9347d60>
                __init__ : <bound method RegionProperties.__init__ of <skimage.measure._regionprops.RegionProperties object at 0x7fb7c9347d60>>
                __init_subclass__ : <built-in method __init_subclass__ of type object at 0x132b970>
                __iter__ : <bound method RegionProperties.__iter__ of <skimage.measure._regionprops.RegionProperties object at 0x7fb7c9347d60>>
                __le__ : <method-wrapper '__le__' of RegionProperties object at 0x7fb7c9347d60>
                __lt__ : <method-wrapper '__lt__' of RegionProperties object at 0x7fb7c9347d60>
                __module__ : skimage.measure._regionprops
                __ne__ : <method-wrapper '__ne__' of RegionProperties object at 0x7fb7c9347d60>
                __new__ : <built-in method __new__ of type object at 0x745800>
                __reduce__ : <built-in method __reduce__ of RegionProperties object at 0x7fb7c9347d60>
                __reduce_ex__ : <built-in method __reduce_ex__ of RegionProperties object at 0x7fb7c9347d60>
                __repr__ : <method-wrapper '__repr__' of RegionProperties object at 0x7fb7c9347d60>
                __setattr__ : <bound method RegionProperties.__setattr__ of <skimage.measure._regionprops.RegionProperties object at 0x7fb7c9347d60>>
                __sizeof__ : <built-in method __sizeof__ of RegionProperties object at 0x7fb7c9347d60>
                __str__ : <method-wrapper '__str__' of RegionProperties object at 0x7fb7c9347d60>
                __subclasshook__ : <built-in method __subclasshook__ of type object at 0x132b970>
                _cache : {}
                _cache_active : True
                _extra_properties : {}
                _image_intensity_double : <bound method RegionProperties._image_intensity_double of <skimage.measure._regionprops.RegionProperties object at 0x7fb7c9347d60>>
                _label_image : [[  1   1   1 ...   0   0   0]
                [  1   1   1 ...   0   0   0]
                [  1   1   1 ...   0   0   0]
                ...
                [  0   0   0 ... 181 181 181]
                [  0   0   0 ... 181 181 181]
                [  0   0   0 ... 181 181 181]]
                _multichannel : False
                _ndim : 2
                _offset : [0 0]
                _pixel_area : 1.0
                _slice : (slice(0, 38, None), slice(0, 28, None))
                _spacing : [1. 1.]
                _spatial_axes : (0, 1)
                area : 849.0
                area_bbox : 1064.0
                area_convex : 880.0
                area_filled : 849.0
                axis_major_length : 43.48415370561371
                axis_minor_length : 26.61485524383126
                bbox : (0, 0, 38, 28)
                centroid : (16.431095406360424, 11.128386336866901)
                centroid_local : [16.43109541 11.12838634]
                coords : [[ 0  0]
                [ 0  1]
                [ 0  2]
                ...
                [37  8]
                [37  9]
                [37 10]]
                coords_scaled : [[ 0.  0.]
                [ 0.  1.]
                [ 0.  2.]
                ...
                [37.  8.]
                [37.  9.]
                [37. 10.]]
                eccentricity : 0.7908123224143987
                equivalent_diameter_area : 32.878265974350796
                euler_number : 1
                extent : 0.7979323308270677
                feret_diameter_max : 45.48626166217664
                image : [[ True  True  True ...  True  True False]
                [ True  True  True ...  True  True False]
                [ True  True  True ...  True  True False]
                ...
                [ True  True  True ... False False False]
                [ True  True  True ... False False False]
                [False  True  True ... False False False]]
                image_convex : [[ True  True  True ...  True  True False]
                [ True  True  True ...  True  True False]
                [ True  True  True ...  True  True  True]
                ...
                [ True  True  True ... False False False]
                [ True  True  True ... False False False]
                [False  True  True ... False False False]]
                image_filled : [[ True  True  True ...  True  True False]
                [ True  True  True ...  True  True False]
                [ True  True  True ...  True  True False]
                ...
                [ True  True  True ... False False False]
                [ True  True  True ... False False False]
                [False  True  True ... False False False]]
                inertia_tensor : [[ 50.28858173  20.21082379]
                [ 20.21082379 112.16280222]]
                inertia_tensor_eigvals : [118.17947646833989, 44.27190747813077]
                label : 1
                moments : [[8.49000000e+02 9.44800000e+03 1.47836000e+05 2.66686000e+06]
                [1.39500000e+04 1.38082000e+05 1.93534200e+06 3.14721580e+07]
                [3.24440000e+05 2.98372400e+06 3.88411760e+07 5.85965876e+08]
                [8.66940000e+06 7.58113120e+07 9.38283216e+08 1.34465352e+10]]
                moments_central : [[ 8.49000000e+02  5.47117907e-13  4.26950059e+04  7.14308371e+04]
                [ 1.32160949e-12 -1.71589894e+04 -1.11861694e+05 -2.23779433e+06]
                [ 9.52262191e+04 -6.28876793e+04  4.76126194e+06  4.89575432e+06]
                [ 2.09153225e+05 -3.66738212e+06 -8.90013562e+06 -4.06008930e+08]]
                moments_hu : [ 1.91344386e-01  7.57813704e-03  8.26088138e-04  2.16245677e-05
                2.19521143e-09  1.37242973e-06 -1.88004013e-09]
                moments_normalized : [[        nan         nan  0.05923272  0.00340108]
                [        nan -0.02380545 -0.00532613 -0.00365677]
                [ 0.13211166 -0.00299431  0.00778035  0.00027456]
                [ 0.00995853 -0.00599285 -0.00049914 -0.00078146]]
                num_pixels : 849
                orientation : -0.28934137007938293
                perimeter : 118.04163056034261
                perimeter_crofton : 114.5920002857185
                slice : (slice(0, 38, None), slice(0, 28, None))
                solidity : 0.9647727272727272

                    """

            # Append the dictionary to the list
            particle_data.append(particle_info)

    # Save the particle data to a CSV file
    csv_file_path = 'ExpFrames/CSVs/cluster_data_frame{}.csv'.format(i)
    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ['Id', 'Centroid_x', 'Centroid_y', 'Area',"Eccentricity"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Write the data
        writer.writerows(particle_data)

    print(f"Particles data for frame {i} has been saved to {csv_file_path}.")
