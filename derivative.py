import numpy as np

# Load data from the txt file
data = np.loadtxt('transect.lldspetr', skiprows=1)

# Extract columns: longitude, latitude, distance, species richness, precipitation, topography,  temp,  temp range
longitude = data[:, 0]
latitude = data[:, 1]
distance = data[:, 2]
species_richness = data[:, 3]
precipitation = data[:, 4]
topo = data[:, 5]
temperature = data[:, 6]
temprange = data[:, 7]


# Function to calculate the absolute derivative
def calculate_derivative(values, distance):
    # create an array of same size as the number of values that we have
    derivative = np.zeros_like(values)
    
    # Use central difference for most points
    for i in range(1, len(values) - 1):
        delta_dist = distance[i + 1] - distance[i - 1]
        if delta_dist != 0:
            derivative[i] = np.abs((values[i + 1] - values[i - 1]) / delta_dist)
    
    # Forward difference for the first point
    delta_dist_first = distance[1] - distance[0]
    if delta_dist_first != 0:
        derivative[0] = np.abs((values[1] - values[0]) / delta_dist_first)
    
    # Backward difference for the last point
    delta_dist_last = distance[-1] - distance[-2]
    if delta_dist_last != 0:
        derivative[-1] = np.abs((values[-1] - values[-2]) / delta_dist_last)
    
    return derivative

# Calculate the derivative for precipitation
derivative_precipitation = calculate_derivative(precipitation, distance)

# Calculate the derivative for topography
derivative_topography = calculate_derivative(topo, distance)

# Calculate the derivative for annual temprature
derivative_temp = calculate_derivative(temperature, distance)

# Calculate the derivative for temprature range
derivative_trange = calculate_derivative(temprange, distance)


# Prepare the output data (distance, derivative_precipitation, derivative_lowresprecipitation)
output_data = np.column_stack((distance, derivative_precipitation,
                               derivative_topography,
                               derivative_temp,
                               derivative_trange))

# Write to a new txt file with all of the cols : distance, ENV varibale 1 der , ENV variable 1 der lower res .....
np.savetxt('derivatives_env.dd', output_data, fmt='%.10f', header='Distance Precipitation Topography Temperature Temprange', comments='')



################ DERIVATIVES OF THE GAUSSIAN SMOOTHED TRANSECTS ####################
# Load data from the txt file
data = np.loadtxt('transect_gauss.lldspetr', skiprows=1)

# Extract columns: distance, precipitation, topography,  temp,  temp range
distance = data[:, 0]
species_richness = data[:, 1]
precipitation = data[:, 2]
topo = data[:, 3]
temperature = data[:, 4]
temprange = data[:, 5]

# Calculate the derivative for precipitation
derivative_precipitation = calculate_derivative(precipitation, distance)

# Calculate the derivative for topography
derivative_topography = calculate_derivative(topo, distance)

# Calculate the derivative for annual temprature
derivative_temp = calculate_derivative(temperature, distance)

# Calculate the derivative for temprature range
derivative_trange = calculate_derivative(temprange, distance)



# Prepare the output data (distance, derivative_precipitation, derivative_lowresprecipitation)
output_data = np.column_stack((distance, derivative_precipitation,
                               derivative_topography,
                               derivative_temp,
                               derivative_trange))

# Write to a new txt file with all of the cols : distance, ENV varibale 1 der , ENV variable 1 der lower res .....
np.savetxt('derivatives_gauss.dd', output_data, fmt='%.10f', header='Distance Precipitation Topography Temperature Temprange', comments='')





