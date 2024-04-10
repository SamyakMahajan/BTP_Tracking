import pandas as pd
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
###TODO please look at the detail abt how the first or last frame number doesnt haver velocity

# Function to calculate magnitude of velocities
def calculate_magnitude_velocity(df, fps=60):
    # Calculate velocities 
    sigma = 7
    step=1
    df['Velocity_x'] = df['Centroid_x'].diff(step) * fps
    df['Velocity_x'] = gaussian_filter1d(df['Velocity_x'], sigma=sigma)
    df['Velocity_y'] = df['Centroid_y'].diff(step) * fps
    df['Velocity_y'] = gaussian_filter1d(df['Velocity_y'], sigma=sigma)

    # Calculate magnitude of velocities
    df['Velocity_Magnitude'] = (df['Velocity_x']**2 + df['Velocity_y']**2)**0.5

    return df

for i in range(1,50 ):
    try:
        df = pd.read_csv('../../results/Cluster_CSVs/keys_data_{}.csv'.format(i))

        if(df.shape[0]<100):
            continue
        
        # Calculate magnitude of velocities
        df = calculate_magnitude_velocity(df)
        
        plt.figure()
        
        # Plot the magnitude of velocities as a function of frame
        plt.plot(df['Frame'], df['Velocity_Magnitude'], label='Cluster {}'.format(i))

        plt.title('Magnitude of Velocities as a Function of Frame(px/s)')
        plt.xlabel('Frame')
        plt.ylabel('Velocity Magnitude')

        # Add legend
        plt.legend()

        # Save the plot to a file (e.g., PNG, PDF, etc.)
        plt.savefig('../btp/Graphs/Velocities/velocity_magnitude_plot_cluster_{}.png'.format(i))
        print("velocity graph of frame",i, "saved")

        # Show the plot (optional)
        # plt.show()

    except Exception as e:
        print(f"Error processing file {i}: {e}")
