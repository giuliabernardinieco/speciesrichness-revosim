import random
import os
import pandas as pd
import re

# Folder Paths
# List of folder paths
folder_paths = ['/REvoSim_output']
# Define folder labels
folder_labels = [15]
# Extract the label from the folder_labels list
label = folder_labels[0]


###################################
### LOGS SPECIES RICHNESS GRIDS ###
###################################

# importing all data from all file so I have a table that I can access later. 
all_grids = []

for i, folder_path in enumerate(folder_paths):
    # creating a loop that will take all of the files, all of the individuals on a transect in the middle of the picture
    # create an empty dataframe to store the transects in the current folder
    grid = pd.DataFrame(columns=['X coord', 'Y coord', 'Species Richness', 'Simulation'])
            
    for filename in os.listdir(folder_path):
        match = re.match(r'REvoSim_individuals_data_.*\.txt', filename)
        if match:
            file_path = os.path.join(folder_path, filename)
            # import file
            df = pd.read_csv(file_path, sep=',', header=0, skiprows=12, usecols=[1, 2, 8])
            df = df[['X coord', 'Y coord', 'species ID']]
            # calculate species richness
            species_count = df.groupby(['Y coord', 'X coord'])['species ID'].nunique().reset_index()
            species_count['Simulation'] = filename
            species_count =species_count.rename(columns={'species ID': 'Species Richness'} )
            
            grid = pd.concat([grid, species_count], ignore_index=True)
            grid['dp'] = folder_labels[i]
            
    # Append the stats dataframe to the list
    all_grids.append(grid)
    
    
# Concatenate all DataFrames from different folders into a single DataFrame
grids = pd.concat(all_grids, ignore_index=True)
# save grids into a csv file
grids.to_csv(f'w50_{label}dp_grids_species_richness.csv')
