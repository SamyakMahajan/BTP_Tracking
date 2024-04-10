import pandas as pd
import matplotlib.pyplot as plt

for i in range(1, 5000):
    try:
        df = pd.read_csv('../btp/Cluster_CSVs/keys_data_{}.csv'.format(i))
        # plt.figure()
        # Plot the trajectory
        if(df.shape[0]<100):
            continue
        # print(df.shape[0])
        plt.plot(df['Centroid_x'], df['Centroid_y'])

        plt.title('Trajectory Plot for Key {}'.format(i))
        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')

        # Save the plot to a file (e.g., PNG, PDF, etc.)
        plt.savefig('../btp/Graphs/Trajectories/trajectory_plot_cluster_{}.png'.format(i))
        print(i, "saved")

    except Exception as e:
        print(f"Error processing file {i}: {e}")
