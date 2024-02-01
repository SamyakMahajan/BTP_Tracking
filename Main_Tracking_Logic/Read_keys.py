import cv2
import pandas as pd
import numpy as np

"""
    Each Frame's clusters are given arbitrary label numbers using connected components analysis.
    We want to destroy this arbitrariness by giving each cluster keys which persists across frames 
"""

def import_keys(csv_file_path):
    df = pd.read_csv(csv_file_path)
    relation=dict(zip(df['Id'].astype(int),df['Key'].astype(int)))
    print(relation)
    
import_keys("Keys_0.csv")