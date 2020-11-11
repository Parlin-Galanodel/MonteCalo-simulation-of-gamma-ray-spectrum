## This project is a simulation of scattered gamma ray spectrum using Monte Carlo method

This project contains **4** files:

***func_const.py*** contains the essential helper functions like formula for compton scattering and Klein-Nishina equation and necessary constants used in the calculation like fine structure constants an pi. The required packages also imported to this file and so both *source.py* and *detector.py* depend on this file.

***source.py*** contains the soure class which abstract the radioactive source.

***detector.py*** contains the detector cleass implement most of the function used to detect and generate a gamma ray spectum.

***MCsimulation.py*** is a sample Monte Carlo simulation use both *source.py* and *detector.py* and it will generate 3 plots for 20, 30 and 45 degrees of scattering angle respectively. 

### if you want to try your own simulation:
you should **import source** and **detector** first and **matplotlib** if you want to plot the graph.
Generate a instance for both source and detector. 
Use detector.setup_source(source) to set up source for the detector.
Prepare a list or dict or numpy.array as a container of the data.
Then generate the data as the for loop do in *MCsimulation.py*.
