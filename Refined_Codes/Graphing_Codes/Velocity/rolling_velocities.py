import pandas as pd
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d

# Function to calculate magnitude of velocities for every 5th centroid value
def calculate_magnitude_velocity(df, fps=60, step=1):
    # Calculate velocities for every 5th centroid value
    sigma = 7
    df['Velocity_x'] = df['Centroid_x'].diff(step) * fps
    df['Velocity_x'] = gaussian_filter1d(df['Velocity_x'], sigma=sigma)
    df['Velocity_y'] = df['Centroid_y'].diff(step) * fps
    df['Velocity_y'] = gaussian_filter1d(df['Velocity_y'], sigma=sigma)

    # Calculate magnitude of velocities
    df['Velocity_Magnitude'] = (df['Velocity_x']**2 + df['Velocity_y']**2)**0.5

    # Calculate smoothed version of velocity magnitude using Gaussian filtering
    sigma = 7  # Adjust the standard deviation as needed
    # df['Smoothed_Velocity_Magnitude'] = gaussian_filter1d(df['Velocity_Magnitude'], sigma=sigma)

    return df

for i in range(1, 5000):
    try:
        df = pd.read_csv('../../results/Cluster_CSVs/keys_data_{}.csv'.format(i))
        if df.shape[0] < 400:
            continue

        # Calculate magnitude of velocities and smoothed version for every 5th centroid value
        df = calculate_magnitude_velocity(df)

        # Create subplots with 2 rows and 1 column
        fig, (ax2, ax1) = plt.subplots(2, 1, sharex=True, figsize=(10, 8))

        # Set the title at the top with increased font size
        fig.suptitle('Comparison of Smooth Speed and Area for cluster {}'.format(i), fontsize=20)

        # Plot the magnitude of velocities and smoothed version as a function of frame on the upper subplot
        ax1.plot(df['Frame'], df['Smoothed_Velocity_Magnitude'], label='Smoothed Velocities Cluster {}'.format(i))
        ax1.set_ylabel('Speed (px/s)', fontsize=20)
        ax1.legend(loc='upper left')

        # Plot 'Area' on the lower subplot
        ax2.plot(df['Frame'], df['Area'], label='Area of Cluster {}'.format(i), color='orange')
        ax2.set_ylabel('Area', fontsize=20)
        ax2.legend(loc='upper left')

        plt.xlabel('Frame', fontsize=20)

        # Save the plot to a file (e.g., PNG, PDF, etc.)
        plt.savefig('../btp/Graphs/Velocities_vs_Area/velocity_magnitude_plot_cluster_{}.png'.format(i))
        print("velocity graph of frame", i, "saved")

        # Show the plot (optional)
        # plt.show()

    except Exception as e:
        print(f"Error processing file {i}: {e}")
