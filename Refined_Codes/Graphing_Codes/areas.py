import pandas as pd
import matplotlib.pyplot as plt

for i in range( 1,7000):
    try:
        df = pd.read_csv('../btp/Cluster_CSVs/keys_data_{}.csv'.format(i))
        if(df.shape[0]<20):
            print("Key",i,"'s life too short to analyse")
            continue

        # Create a new figure for each iteration
        plt.figure()

        # Plot the area as a function of frame
        plt.plot(df['Frame'], df['Area'], label='Cluster {}'.format(i))

        plt.title('Area vs Frame Number(time) for cluster {}'.format(i))
        plt.xlabel('Frame')
        plt.ylabel('Area')

        # Add legend
        # plt.legend()

        # Save the plot to a file (e.g., PNG, PDF, etc.)
        plt.savefig('../btp/Graphs/Areas/area_plot_clusters{}.png'.format(i))
    
        print(i, "saved")

        # Show the plot (optional)
        # plt.show()

    except Exception as e:
        # print(f"Error processing file {i}: {e}")
        continue

