# :microbe: REvoSim to study the relationship between species richness and environment

This file contains instructions on:

- How to generate the environment file
- How to run a simulation in REvoSim with dispersion parameter = 15
- How to generate results analogous to Figure 4a-f

## Generating the environment file
- Run the environment.py file to get the png file that will be used as the environment from REvoSim

## Running a Simulation
REvoSim can be run via the command line or using the user interface (GUI).
Instructions on how to install and run REvoSim can be found [here](https://revosim.readthedocs.io/en/latest/).

Once the Program is installed, open it, go to Settings > Environmental settings > Change Environment file and upload the png file you created before. 

To run the simulation so that all tunable parameters are set as described in the manuscript, go to Commands > Load Settings and select the REvoSim_settings_15dp_image.xml file. 

To produce the v2.0.0 CSV logs, as the output of your simulation, go to Logging, click on the v2.0.0 CSV logs button and tick the 'Write to file' box.

The simulation is now ready to start, Click on the button 'run for' and enter 100,000 in the dialogue box. Batches of simulations can be run one after the other by using the 'Batch' button. 

Detailed instructions on how to run REvoSim from the command line are to be found in the [REvoSim manual](https://revosim.readthedocs.io/en/latest/).

## Analysing 3000 replicates
The file fetc

