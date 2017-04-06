
import numpy as np
import statistics as stat

def temp_calcs():

    fileobj = open('test.txt', 'r')
    fileobj.readline()
    fileobj.readline()
    fileobj.readline()
    parser = fileobj.readline()
    data = parser.split('\t')
    print(data)
    for line in fileobj: #this should append values by index.
        parser = fileobj.readline()
        a = parser.split('\t')
        print(a)
        if a[0] == '\n':
            continue
        if '\n' in a[0]:
            data.append(a[0])
            data.append('')
            data.append('')
            data.append('')
            continue
        data.append(a[0])
        if a[1] == '\n':
            data.append('')
            data.append('')
            data.append('')
            continue
        if '\n' in a[1]:
            data.append(a[1])
            data.append('')
            data.append('')
            continue
        data.append(a[1])
        if a[2] == '\n':
            data.append('')
            data.append('')
            continue
        if '\n' in a[2]:
            data.append(a[2])
            data.append('')
            continue
        data.append(a[2])
        if a[3] == '\n':
            data.append('')
            continue
        data.append(a[3])
    result = np.ma.masked_array(data, mask = '')
    print(result)

    temperature = list()
    for index in range(0,len(result)):
        print(index)
        if (int(index) % 3 is 0) and (int(index) is not 0):
            print(result[index])
            temperature.append(float(result[index]))
    #print(temperature)

 #   mean = np.mean(temperature)
 #   median = np.median(temperature)
 #   standard_deviation = np.std(temperature)

 #   print("Mean:")
 #   print(mean)
 #   print("Median:")
 #   print(median)
 #   print("Standard Deviation:")
 #   print(standard_deviation)







temp_calcs()

#missing values show up as ''
#  or '\n' in newline.