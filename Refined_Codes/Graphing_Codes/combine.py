import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate magnitude of velocities
def calculate_magnitude_velocity(df, fps=60):
    # Calculate velocities
    df['Velocity_x'] = df['Centroid_x'].diff() * fps
    df['Velocity_y'] = df['Centroid_y'].diff() * fps

    # Calculate magnitude of velocities
    df['Velocity_Magnitude'] = (df['Velocity_x']**2 + df['Velocity_y']**2)**0.5

    return df

# Create a figure with three subplots
fig, axes = plt.subplots(3, 1, figsize=(10, 15))

# Plot Trajectories
axes[0].set_title('Trajectory Plots')
for i in range(1, 250):
    try:
        df = pd.read_csv('../btp/Cluster_CSVs/keys_data_{}.csv'.format(i))
        axes[0].plot(df['Centroid_x'], df['Centroid_y'], label='Cluster {}'.format(i))
    except Exception as e:
        print(f"Error processing file {i}: {e}")

# Plot Velocities
axes[1].set_title('Magnitude of Velocities as a Function of Frame (px/s)')
for i in range(1, 250):
    try:
        df = pd.read_csv('../btp/Cluster_CSVs/keys_data_{}.csv'.format(i))
        df = calculate_magnitude_velocity(df)
        axes[1].plot(df['Frame'], df['Velocity_Magnitude'], label='Cluster {}'.format(i))
    except Exception as e:
        print(f"Error processing file {i}: {e}")

# Plot Areas
axes[2].set_title('Area as a Function of Frame')
for i in range(1, 250):
    try:
        df = pd.read_csv('../btp/Cluster_CSVs/keys_data_{}.csv'.format(i))
        axes[2].plot(df['Frame'], df['Area'], label='Cluster {}'.format(i))
    except Exception as e:
        print(f"Error processing file {i}: {e}")

# Set common labels
for ax in axes:
    ax.set_xlabel('Frame')

# Add legends
axes[0].legend()
axes[1].legend()
axes[2].legend()

# Save the plot to a file (e.g., PNG, PDF, etc.)
plt.savefig('../btp/Graphs/combined_plots.png')

# Show the plot (optional)
plt.show()
