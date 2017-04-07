
#=======================================================================
#                        General Documentation

"""Single-function module.

   See function docstring for description.
"""

#-----------------------------------------------------------------------
#                       Additional Documentation

#
# Modification History:
# - 6 April 2017:  Original by Peter Stanton,
#   University of Washington Bothell.
#
# Notes:
# - Written for Python 3.6.0
# - See import statements throughout for more information on non-
#   built-in packages and modules required.
# - Currently not functioning
# - Data file should terminate with last line of data, not a blank, empty line.
#
# Copyright (c) 2017-2018 by Peter Stanton.
# Documentation template provided by Johnny Lin, for more information see
# the URL http://www.johnny-lin.com/py_pkgs/atmqty/doc/.
#=======================================================================


#---------------- Module General Import and Declarations ---------------

import numpy as np
import matplotlib.pyplot as plt

#-------------------- General Function:  temp_calcs ---------------------

def temp_calcs():
    """Calculate surface temperature data.

       Method Arguments:
       * variables:  A file object that accesses a data set consisting of
            Julian day, longitude, latitude, and surface temperature in
            Celsius:
         + 'fileObj':  Accesses data file
         + 'parser':   String that holds each data point as it is retrieved
         + 'data':     A list that holds the elements of the data points, separated.
         + 'result':   The list is transformed into a masked array of floats that
                        conceals missing values with masking
         + 'temperature': A list used to contain just the temperature measurements to determine
                          basic descriptive statistics: mean, median, standard deviation.
                          
       Output:
       * Mean. The average of all temperatures taken in this data set.
       * Median. The median of all temperatures in this data set.
       * Standard deviation. The standard deviation of the temperatures recorded.
       * Line graph. A graph showing Julian Day on the x-axis plotted against temperature.

       Reference:
       * Lin, J. (2017):  Python: Files, Masks, and Plotting.  
            https://canvas.uw.edu/courses/1151937/assignments/3653728
        """
    fileobj = open('test.txt', 'r')
    fileobj.readline()
    fileobj.readline()
    fileobj.readline()
    parser = fileobj.readline()
    data = parser.split('\t')
    print(data)
    for line in fileobj: #this should append values by index.
        a = line.split('\t')
        print(a)
        if a[0] == '\n':
            continue
        if '\n' in a[0]:
            data.append(a[0])
            data.append(9000000)
            data.append(9000000)
            data.append(9000000)
            continue
        data.append(a[0])
        if a[1] == '\n':
            data.append(9000000)
            data.append(9000000)
            data.append(9000000)
            continue
        if '\n' in a[1]:
            data.append(a[1])
            data.append(9000000)
            data.append(9000000)
            continue
        data.append(a[1])
        if a[2] == '\n':
            data.append(9000000)
            data.append(9000000)
            continue
        if '\n' in a[2]:
            data.append(a[2])
            data.append(9000000)
            continue
        data.append(a[2])
        if a[3] == '\n':
            data.append(9000000)
            continue
        data.append(a[3])
    result = np.ma.masked_array(data, mask=data[<=9000000])
    print(result)

    temperature = list()
    key = 3
    for index in range(0,len(result)):
        print(index)
        if (index == key):
            if result[index] == '':
                key += 4
                continue
            print(result[index])
            temperature.append(float(result[index]))
            key += 4
    print(temperature)


    julian_day = list()
    key = 0
    for index in range(0,len(result)):
        print(index)
        if (index == key):
            if result[index] == '':
                key += 4
                continue
            print(result[index])
            julian_day.append(float(result[index]))
            key += 4
    print(julian_day)
    mean = np.mean(temperature)
    median = np.median(temperature)
    standard_deviation = np.std(temperature)

    print(np.shape(temperature))
    print(np.shape(julian_day))

    print("Mean:")
    print(mean)
    print("Median:")
    print(median)
    print("Standard Deviation:")
    print(standard_deviation)



    plt.plot(julian_day, temperature)
    plt.axis([min(julian_day), max(julian_day), min(temperature), max(temperature)])
    plt.xlabel("Julian Day")
    plt.ylabel("Temperature in Celsius")
    plt.show()






temp_calcs()

#missing values show up as ''
#  or '\n' in newline.