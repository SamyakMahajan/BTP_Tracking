import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

for i in range(1,50):
    # Step 1: Read the CSV file
    df = pd.read_csv('results/CSVs/cluster_data_frame{}.csv'.format(i))  # Replace 'path_to_your_file.csv' with your file path
    # Step 2: Plot the probability distribution of the 'Eccentricity' column
    sns.histplot(df['Area'], kde=True, stat="density", linewidth=0, bins=50)
    plt.title('Probability Distribution of Area for frame {}'.format(i))
    plt.xlabel('Area')
    plt.ylabel('Density')
    plt.savefig('results/Graphs/Area_distributions/Area_distribution_{}.png'.format(i), dpi=300)  # Saves the plot in the current working directory
    # plt.clf()

#random frame eccentricity
#2d hist all frames
#Area distribution per frsme