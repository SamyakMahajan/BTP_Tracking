import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

for i in range(1,50):
    # Step 1: Read the CSV file
    df = pd.read_csv('results/CSVs/cluster_data_frame{}.csv'.format(i))  # Replace 'path_to_your_file.csv' with your file path
    # Step 2: Plot the probability distribution of the 'Eccentricity' column
    df['Area']=df['Area']/300
    sns.histplot(df['Area'], kde=True, linewidth=0 ,binwidth=1,element='step')
    plt.title('Probability Distribution of Area for frame {}'.format(i))
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Area')
    plt.ylabel('Density')
    plt.savefig('results/Graphs/Area/Area_distributions2/Area_distribution_{}.png'.format(i), dpi=300)  # Saves the plot in the current working directory
    plt.clf()

#random frame eccentricity
#2d hist all frames
#Area distribution per frsme

#cumulative area distribution
#Log log with 