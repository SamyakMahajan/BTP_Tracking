import pandas as pd
import matplotlib.pyplot as plt

for i in range(1, 50):
    # Step 1: Read the CSV file
    file_path = 'results/CSVs/cluster_data_frame{}.csv'.format(i)
    df = pd.read_csv(file_path)

    # Step 2: Plot Eccentricity vs. Area scatter plot
    plt.scatter(df['Eccentricity'], df['Area'])

    plt.title('Eccentricity vs. Area')
    plt.xlabel('Eccentricity')
    plt.ylabel('Area')
    
    # # Step 3: Save the plot as a PNG file
    plt.savefig('results/Graphs/eccvsA/eccentricity_area_{}.png'.format(i), dpi=300)

    # Clear the current figure for the next plot
    plt.clf()


    # Step 3: Save the plot as a PNG file
# plt.savefig('../Graphs/eccvsA/eccentricity_area.png', dpi=300)
