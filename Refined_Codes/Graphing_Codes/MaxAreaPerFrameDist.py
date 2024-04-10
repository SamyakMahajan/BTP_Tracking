import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Initialize lists to store Area data
area_list = []

# Loop through each CSV file and accumulate Area data
for i in range(1, 50):
    # Step 1: Read the CSV file
    file_path = f'results/CSVs/cluster_data_frame{i}.csv'
    df = pd.read_csv(file_path)
    max_area = df['Area'].max()

    # Append the maximum area for the current dataframe to the list
    area_list.append(max_area)

# Convert the list to a numpy array for plotting
area_array = np.array(area_list)

# Plot Max Area Per Frame
plt.figure(figsize=(12, 6))  # Adjust figure size as needed

# Plotting the data points
plt.plot(range(1, 50), area_array, marker='o', linestyle='-', color='b')

plt.title('Max Area Per Frame')
plt.ylabel('Area')
plt.xlabel('Frame Number')

# Rotating x-axis labels for better readability
plt.xticks(rotation=45)

# Save the plot as a PNG file
plt.savefig('results/Graphs/MaxArea/Max_area.png', dpi=300)

# Optionally clear the current figure
plt.clf()