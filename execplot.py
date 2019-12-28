o#!/usr/bin/python
#
#execplot.py
# Plot genetator for anemometric station datalogger data analysis csv sourced by statistics of the day:24h, 144@logs/10min. Sample voltage(V) and current(I).
#Shine on source: https://codinginfinite.com/data-visualizing-csv-format-chart-using-python-matplotlib/
#$ python execplot.py
import csv
from matplotlib import pyplot as plt
filename = 'execplot.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    avgs = []
    for row in reader:
        if row[17]=='': # choose column value
            continue
        avg = float(row[17]) # choose column value
        avgs.append(avg)  #appending avg value   
    
    #Plot Data
    fig = plt.figure(dpi = 100, figsize = (10,6)) # line resolution and ratio
    plt.plot(avgs, lw = 0.5, c = 'blue') #Line width and color

    #Format Plot 
    #select title and date  
    #plt.title("AV current D154004, 12-15-2019", fontsize = 12)
    plt.title("AV voltage D154004, 12-15-2019", fontsize = 12)

    plt.xlabel('Statistics of the day:24h, 144@logs 10min', fontsize = 6) #update if need

    #select ylabel type
    #plt.ylabel("DL current (I)", fontsize = 8)
    plt.ylabel("DL voltage (V)", fontsize = 8)

    plt.tick_params(axis = 'both', which = 'major' , labelsize = 10)

    #adjust ylim according to the values
    #plt.ylim(44, 140) #ylim current (I)
    plt.ylim(10, 14)   #ylim voltage (V)
    plt.show()
