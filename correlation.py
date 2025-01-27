import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import matplotlib.cm as cm
import matplotlib.colorbar as colorbar
import matplotlib.colors as colors

# The following data contains the gaussian smoothed data of the environmental variables
data_gauss = np.loadtxt('transect_gauss.lldspetr',  skiprows=1)

# extract gaussian smoothed variables columns: , precipitation, topography,  temp,  temp range
distance = data_gauss[:, 0]
species_richness = data_gauss[:, 1]
precipitation = data_gauss[:, 2]
topo = data_gauss[:, 3]
temperature = data_gauss[:, 4]
temprange = data_gauss[:, 5]


#  The following contains the derivative of the environmental variables
data_der = np.loadtxt('derivatives_env_gauss.lldspetr', skiprows=1)

# extract derivative columns: precipitation, topography,  temp,  temp range
precipitation_der = data_der[:, 1]
topo_der = data_der[:, 2]
temperature_der = data_der[:, 3]
temprange_der = data_der[:, 4]


# Variables to correlate with sr and their names
variables_to_correlate = {
    "precipitation": precipitation,
    "topography": topo,
    "temperature": temperature,
    "temperature_range": temprange,
    "derivative_precipitation": precipitation_der,
    "derivative_topography": topo_der,
    "derivative_temperature": temperature_der,
    "derivative_temperature_range": temprange_der
}

################ CORRELATION COEFFIECIENTS BETWEEN THE GAUSSIAN SMOOTHED DERIVATIVES ANS PECIES RICHNESS ####################
# Create a table
results = []
print("Correlation coefficients with species richness:")
for name, variable in variables_to_correlate.items():
    correlation = np.corrcoef(species_richness, variable)[0, 1]
    pvalue = linregress(species_richness, variable).pvalue
    print(f"{name} {correlation:.3f}  {pvalue:.2e} **p<0.05** " if pvalue < 0.05 else f"{name} {correlation:.3f}  {pvalue:.2e} p>0.05")
    results.append([name, correlation, pvalue])

# Prepare the output file
with open('correlation_results.txt', 'w') as f:
    # Write header
    f.write("Variable Correlation pvalue Significance\n")
    
    # Write each variable's name and its correlation
    for name, correlation, pvalue in results:
        f.write(f"{name} {correlation:.2f} {pvalue:.2e} **p<0.05**\n" if pvalue < 0.05 else f"{name} {correlation:.3f}  {pvalue:.2e} p>0.05\n")