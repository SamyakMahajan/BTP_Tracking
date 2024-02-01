import cv2
import pandas as pd
import numpy as np

"""
    This script tries to find out the children of each Cluster
"""


def import_keys(csv_file_path):
    df = pd.read_csv(csv_file_path)
    relation=dict(zip(df['Id'].astype(int),df['Key'].astype(int)))
    return relation    

def Find_Children(image_path, csv_file_path, output_path):
    # Read the original image
    Label_key_relation=import_keys('Keys_0.csv')
    print(Label_key_relation)
    image = cv2.imread(image_path)
    children={}
    # Read center coordinates from the CSV file
    df = pd.read_csv(csv_file_path)
    center_coordinates = list(zip(df['Centroid_x'].astype(int), df['Centroid_y'].astype(int),df['Id'].astype(int)))

    # Overlay red dots on the image
    for cx, cy, Id in center_coordinates:
        # Draw a red dot on the image
        # cv2.circle(image, (cx, cy), radius=3, color=(0, 0, 255), thickness=-1)  # -1 fills the circle
        parent_label=image[cy,cx][0]
        try:
            parent_key=Label_key_relation[parent_label]
            print("Cluster {} in Image 2 lies in".format(Id), "Cluster", parent_label, "Of Image 1 and has Parent_key:",parent_key)
            
            if(parent_key not in children.keys()):
                children[parent_key]=[]
            children[parent_key].append(Id)
        except:
            """
                THIS NEEDS FIXING!!!
                Traceback (most recent call last):
                File "/home/samyak/Downloads/BTP_Tracking_v0/Main_Tracking_Logic/Find_Children.py", line 45, in <module>
                    Find_Children(image_path, csv_file_path, output_path)
                File "/home/samyak/Downloads/BTP_Tracking_v0/Main_Tracking_Logic/Find_Children.py", line 29, in Find_Children
                    print("Cluster {} in Image 2 lies in".format(Id), "Cluster", parent_label, "Of Image 1 and has Parent_key:",Label_key_relation[parent_label])
                KeyError: 0
            """
            continue
        # children[Parent_key].append(Id)
    # Save the image with overlaid red dots
    # cv2.imwrite(output_path, image)
    print(children)
    """
        We get children dictionary like this
            where the key represents the parent(i.e. the key of the cluster in the previous frame) 
            and the value corresponding to the key is the list of labels of clusters in the current frame whose centroids lie in the region of the key in the previous frame. We call them children of the parent cluster 
        {1: [1], 2: [2], 4: [3], 5: [4], 3: [5], 6: [6], 7: [7], 8: [8], 9: [9], 11: [10], 
        12: [11], 10: [12], 14: [13], 15: [14], 13: [15], 16: [16], 19: [17], 17: [18], 
        18: [19], 20: [20], 21: [21], 22: [22], 24: [23], 23: [24], 25: [25], 26: [26],
        27: [27], 28: [28], 29: [29], 30: [30], 31: [31], 33: [32], 32: [33], 34: [34], 
        35: [35], 36: [36], 38: [37], 37: [38], 39: [39], 40: [40], 41: [41], 42: [42], 
        44: [43], 43: [44], 45: [45], 47: [46], 49: [47], 46: [48], 50: [49], 51: [50], 
        48: [51], 52: [52], 53: [53], 54: [54], 55: [55], 56: [56], 57: [57], 58: [58], 
        59: [59], 61: [60], 60: [61], 62: [62], 63: [63], 66: [64], 64: [65], 65: [66], 
        67: [67, 69], 68: [68], 69: [70], 70: [71], 71: [72], 73: [73], 74: [74], 75: [75],
        77: [76], 76: [77], 78: [78], 79: [79], 81: [80], 80: [81], 82: [82], 83: [83], 84: [84], 85: [85], 86: [86], 87: [87], 89: [88], 88: [89], 90: [90], 91: [91], 92: [92], 95: [93], 93: [94], 94: [95], 96: [96], 97: [97], 98: [98], 99: [99], 100: [100], 101: [101], 102: [102], 103: [103], 105: [104], 104: [105], 106: [106], 107: [107], 108: [108], 109: [109], 112: [110], 119: [111, 119], 111: [112], 116: [113], 113: [114], 115: [115], 114: [116], 117: [117], 118: [118], 120: [120], 121: [121], 122: [122], 124: [123], 123: [124], 126: [125, 133], 125: [126], 127: [127], 128: [128], 129: [129], 132: [130], 130: [131], 131: [132], 134: [134], 133: [135], 135: [136], 136: [137], 137: [138], 138: [139], 140: [140], 139: [141], 141: [142], 142: [143], 143: [144], 144: [145], 145: [146], 146: [147, 154], 148: [148], 147: [149], 149: [150], 150: [151], 151: [152], 152: [153], 154: [155], 155: [156], 157: [157], 156: [158], 158: [159], 159: [160], 161: [161], 160: [162], 162: [163, 173], 163: [164], 165: [166], 167: [167], 166: [168], 169: [169], 168: [170], 171: [171], 170: [172], 173: [174], 174: [175], 176: [176], 175: [177], 177: [178], 178: [179], 181: [180], 179: [181], 183: [182], 180: [183], 182: [184], 185: [185], 184: [186], 186: [187], 187: [188]}

    """
    
    for parent in children.keys():
        if(len(children[parent])>1):
            print(parent,":",children[parent])
    """
        We get the following clusters who have more than one children.
        This indicates that they have "MOST PROBABLY" broken down into more parts ,
        and we will next have to deal with the issue of choosing which of the children is called successor with the same key.
        Children other than the successor would have to be given entirely new keys

        67 : [67, 69]
        119 : [111, 119]
        126 : [125, 133]
        146 : [147, 154]
        162 : [163, 173]

    """
for i in range(1):
#     image_path = '../BTP4/Labeled_Images/labeled_image_1.png'
# csv_file_path = '../BTP4/CSVs/particle_data_Img_2.csv'
# output_path = 'centroids_of_Img_2_on_labeled_image_1.jpg'

    image_path = '../BTP4/Labeled_Images/labeled_image_{}.png'.format(i)
    csv_file_path = '../BTP4/CSVs/particle_data_Img_{}.csv'.format(i+1)
    output_path = 'Centroids_On_Labeled_Previous_Image/centroids_of_Img_{}_on_labeled_image_{}.jpg'.format(i+1,i)
    Find_Children(image_path, csv_file_path, output_path)

print("completed!")