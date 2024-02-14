#2. (20 points) Write a Python function `graphSnowfall(t)` which retrives data in a text file _t_ and displays that information in a bar chart.
#I used numpy because it is the most efficient and easy way to arrange it into ranges without writting multiple lines of code and then it can convert the histogram data to bar graph 

import numpy as np
import matplotlib.pyplot as plt

def graphSnowfall(t):
    # Read the data from the text file into a NumPy array
    snowfall_data = np.loadtxt(t)  # Assuming the data is in a simple text file format

    # Define the ranges for snowfall aggregation
    ranges = [0, 10, 20, 30, 40, 50]

    # Aggregate the snowfall values into the specified ranges
    #snowfall_aggregate to store the histogram values, and the underscore _ is used to discard the bin edges, as they are not needed for the bar chart.
    snowfall_aggregate, _ = np.histogram(snowfall_data, bins=ranges)

    # Plot the snowfall data as a bar chart
    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    plt.bar([f"{ranges[i]}-{ranges[i+1]} cm" for i in range(len(ranges)-1)], snowfall_aggregate)
    plt.xlabel('Snowfall Range')
    plt.ylabel('Frequency')
    plt.title('Snowfall Data')
    plt.show()
    plt.savefig('snow.png')
  
