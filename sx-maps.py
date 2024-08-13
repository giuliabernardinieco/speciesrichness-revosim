
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.gridspec as gridspec
import matplotlib.image as mpimg


# Combined transect file, contais all x and y position and their number of species
combined_transects = pd.read_csv('w50_15dp_grids_species_richness.csv', sep=',', index_col=0)
print(combined_transects.head())

# Get Blue values as read by Revosim from one of the Simulation logs that you have run .
colsin = pd.read_csv('REvoSim_individuals_data.txt', sep=',', header=0, skiprows=12, usecols=[1, 2, 11]).drop_duplicates(subset=['X coord', 'environment B value'])

# Filter to remove simulations thta have not reached the end
cells = combined_transects.groupby('Simulation').apply(lambda group: group[['X coord', 'Y coord']].drop_duplicates().shape[0])
print(f'There are {cells[cells <= 1].shape[0]} simulations with less than the full grid cell')

# Calculate species richness for each simulation and each X position
sims_means = combined_transects.groupby(['Simulation', 'X coord'])['Species Richness'].mean().reset_index()
print(sims_means.head())

# Calculate the mean species richness for each X and Y position for all simulations ('mean grid')
transects_100 = combined_transects.groupby(["Y coord", 'X coord'])['Species Richness'].mean().reset_index()

# Pivot the data to create an heatmap
pivot_mean = combined_transects.pivot_table(index='Y coord', columns='X coord', values='Species Richness', aggfunc='mean')

# Replace NaN values with 0
pivot_mean = pivot_mean.fillna(0)

# Create a map and extract color bar
to_get_from = sns.heatmap(pivot_mean, cmap='BuPu', square=True)
# Get the colorbar from the heatmap
colorbar = to_get_from.collections[0].colorbar

# Derivative of Environment
##### HEATMAP OF THE DERIVATIVE OF THE ENVIRONMENT FUNCTION
wavelength = 50  # define the variable that contains the wavelength
devsin = (255 * np.pi * abs(np.cos(2 * np.pi * (np.arange(0, 100, 1) / wavelength)))) / wavelength  # derivative of the environment function
# Create a DataFrame with 100 rows and 100 columns
pivot_dev = pd.DataFrame([devsin] * 100)


######################
### PANEL CREATION ###
######################
# Load the image to get its dimensions
img = mpimg.imread('w50_0RG.png')


# Create a figure
fig = plt.figure(figsize=(9, 4))
# Create a grid layout
GridSpec = gridspec.GridSpec(ncols=4, nrows=1, figure= fig, width_ratios=[1, 0.99, 1, 0.28], wspace=0.00, hspace=0.0, top=0.0, bottom=0.0, left=0.0, right=0.0)

# Set the x-axis tick positions and labels
x_ticks = [0, 20, 40, 60, 80]  # Define the positions of the ticks
x_tick_labels = ['0', '20', '40', '60', '80']  # Define the labels for the ticks

####### SUBFIGURE ONE, TAKING THE FIRST COLOUMN
subfig1 = fig.add_subfigure(GridSpec[:, 0] )
# adding 2 plots for the suplots
subplots1 = subfig1.subplots(nrows=2, ncols=1, height_ratios=[3, 1], sharex=True)
subfig1.subplots_adjust(wspace=0, hspace=0.2)
# plot 1 -upper
subplots1[0].imshow(img)
subplots1[0].axis('off')
#subplots1[0].text(0.5, 1.03, 'Environment (w=50)', horizontalalignment='center', verticalalignment='bottom', transform=subplots1[0].transAxes, fontsize=14)
# annotate two axes
subplots1[0].annotate('', xy=(6, 70), xytext=(6, 94.8), arrowprops=dict( lw=2, facecolor='white', edgecolor='white', arrowstyle='->'), zorder=3)
subplots1[0].annotate('', xy=(5.8, 93.7), xytext=(30, 93.7), arrowprops=dict(lw =2, facecolor='white', edgecolor='white', arrowstyle='<-'), zorder=3)
subplots1[0].text(0.05, 0.18, 'y', transform=subplots1[0].transAxes, fontsize=8,  va='top', ha='right', color='white', weight='bold')
subplots1[0].text(0.18, 0.052, 'x', transform=subplots1[0].transAxes, fontsize=8,  va='top', ha='right', color='white', weight='bold')
# plot 1 -lower
sns.lineplot(data=colsin, x='X coord', y='environment B value', color="blue", ax=subplots1[1])
subplots1[1].set_ylim(0, 270)
subplots1[1].set_xlabel('$X$ Coordinate')
subplots1[1].set_ylabel('Environment,$e$')


####### SUBFIGURE TWO, TAKING THE CENTRAL COLOUMN
subfig2 = fig.add_subfigure(GridSpec[:, 1])
# adding 2 plots for the suplots
subplots2 = subfig2.subplots(nrows=2, ncols=1, height_ratios=[3, 1], sharex=True)
# plot 2 -Upper
sns.heatmap(pivot_dev, cmap='Greys', ax=subplots2[0], cbar=False, square=True)
subplots2[0].axis('off')
#subplots2[0].text(0.5, 1.03, 'Derivative (abs)', horizontalalignment='center', verticalalignment='bottom', transform=subplots2[0].transAxes, fontsize=14)
# plot 2 - Lower
subplots2[1].plot(list(range(0, 100)), devsin, color="black")
# subplots2[1].set_ylim(0, 270)
# subplots2[1].set_yticks([])
subplots2[1].set_xlabel('$X$ Coordinate')
subplots2[1].set_ylabel('${|\\dot{e}|}$') #labelpad=-1
subplots2[1].set_xticks(x_ticks)
subplots2[1].set_xticklabels(x_tick_labels)


####### SUBFIGURE THREE, TAKING THE RIGHT COLOUMN
subfig3 = fig.add_subfigure(GridSpec[:, 2])
# adding 2 plots for the suplots

subplots3 = subfig3.subplots(nrows=2, ncols=1, height_ratios=[3, 1], sharex=True)
# plot 3 - Upper
sns.heatmap(pivot_mean, cmap='BuPu', ax=subplots3[0], square=True, cbar=False)
subplots3[0].axis('off')
#subplots3[0].text(0.5, 1.03, 'Average Species Richness', horizontalalignment='center', verticalalignment='bottom', transform=subplots3[0].transAxes, fontsize=14)
# plot 3 - Lower
sns.lineplot(data=transects_100, x='X coord', y='Species Richness', hue='Y coord', palette = 'Greys', errorbar=None, legend=False, alpha=0.1, linewidth = 0.5)
sns.lineplot(data=combined_transects, x='X coord', y='Species Richness', color=sns.color_palette('viridis')[0], ax=subplots3[1], errorbar=None)
subplots3[1].set_xlabel('$X$ Coordinate')
subplots3[1].yaxis.tick_right()
subplots3[1].yaxis.set_label_position("right")
subplots3[1].set_ylabel('  Species \n Richness')
subplots3[1].set_xticks(x_ticks)
subplots3[1].set_xticklabels(x_tick_labels)
####### SUBFIGURE FOUR, LEGEND COLOUMN
subfig4 = fig.add_subfigure(GridSpec[:, 3])
subplots4 = subfig4.subplots(nrows=2, ncols=1, height_ratios=[3, 1])
subplots4[0].axis('off')
cb = plt.colorbar(to_get_from.get_children()[0], ax=subplots4[0], label=colorbar.ax.yaxis.label.get_text(), pad=0.5, location='left')
# Set the ticks on the right side
cb.ax.yaxis.set_ticks_position('right')
subplots4[1].axis('off')

letters = ['a', 'b', 'c', 'd', 'e', 'f']
for i, ax in enumerate([subplots1[0], subplots2[0], subplots3[0]]):
    ax.annotate(letters[i], xy=(0.96, 0.96), xycoords='axes fraction', fontsize=11,
                horizontalalignment='right', verticalalignment='top',
                bbox=dict(boxstyle='square', facecolor='white', edgecolor='black'))

letters = [ 'd', 'e', 'f']
for i, ax in enumerate( [subplots1[1], subplots2[1], subplots3[1]]):
    ax.annotate(letters[i], xy=(0.95, 0.9), xycoords='axes fraction', fontsize=11,
                horizontalalignment='right', verticalalignment='top',
                bbox=dict(boxstyle='square', facecolor='white', edgecolor='black'))


fig.savefig('figure-4_high_res.png', dpi=300, bbox_inches='tight')