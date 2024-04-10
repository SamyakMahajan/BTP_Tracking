import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Initialize a MinMaxScaler to normalize values to the [0, 1] range
scaler = MinMaxScaler()

for i in range(1, 50):
    # Step 1: Read the CSV file
    df = pd.read_csv(f'results/CSVs/cluster_data_frame{i}.csv')
    
    # Normalize 'Area' and 'Eccentricity' separately
    df['Normalized Area'] = scaler.fit_transform(df[['Area']])
    df['Normalized Eccentricity'] = scaler.fit_transform(df[['Eccentricity']])
    
    # Step 2: Plot the probability distribution of the normalized 'Area' and 'Eccentricity'
    plt.figure(figsize=(10, 6))  # Set a larger figure size for clarity
    
    # Plot normalized Area
    sns.histplot(df['Normalized Area'], kde=True, stat="density", linewidth=0, bins=50, color="blue", label="Area", alpha=0.5)
    
    # Plot normalized Eccentricity
    sns.histplot(df['Normalized Eccentricity'], kde=True, stat="density", linewidth=0, bins=50, color="red", label="Eccentricity", alpha=0.5)
    
    plt.title(f'Probability Distribution of Normalized Area and Eccentricity for Frame {i}')
    plt.xlabel('Normalized Value')
    plt.ylabel('Density')
    plt.legend()
    
    plt.savefig(f'results/Graphs/combinedDistributions/normalized_distribution_{i}.png', dpi=300)
    plt.clf()
