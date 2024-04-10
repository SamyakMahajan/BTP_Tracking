import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Initialize lists to store Eccentricity and Area data
eccentricity_list = []
area_list = []

# Loop through each CSV file and accumulate Eccentricity and Area data
for i in range(1, 50):
    # Step 1: Read the CSV file
    file_path = f'results/CSVs/cluster_data_frame{i}.csv'
    df = pd.read_csv(file_path)
    
    # Append the data from the current dataframe to the lists
    eccentricity_list.extend(df['Eccentricity'])
    area_list.extend(df['Area'])

# Convert lists to numpy arrays for plotting
eccentricity_array = np.array(eccentricity_list)
area_array = np.array(area_list)

# Plot Eccentricity vs. Area as a 2D heatmap
plt.figure(figsize=(8, 6))  # Adjust figure size as needed
# Determine bin edges
ecc_bins = np.linspace(eccentricity_array.min(), eccentricity_array.max(), 20)
area_bins = np.linspace(area_array.min(), area_array.max(), 20)
plt.hist2d(eccentricity_array, area_array, bins=[ecc_bins, area_bins], cmap='plasma', cmin=1)
plt.colorbar(label='Count')  # Show a color bar indicating the counts in each bin

plt.title('Accumulated Eccentricity vs. Area Heatmap')
plt.xlabel('Eccentricity')
plt.ylabel('Area')

# Save the plot as a PNG file
plt.savefig('results/Graphs/eccvsA/eccentricity_area_heatmap_accumulated_plasma.png', dpi=300)

# Optionally clear the current figure
plt.clf()
