#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Graph Helper Functions
# By Nick Erickson

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math
    
def graphSimple(xList, yList, namesList, title, ylabel, xlabel, savefigName=""):
    colors = iter(cm.rainbow(np.linspace(0, 1, len(yList))))                
    plt.figure()
    maxY = 0
    maxX = 0
    minY = 9999999999999999999999999999999999999999999999999999999999999
    minX = 9999999999999999999999999999999999999999999999999999999999999
    for i in range(len(yList)):
        color = next(colors)
        name = namesList[i]
        y = yList[i]
        x = xList[i]
    
        maxY = max(maxY, np.max(y))
        minY = min(minY, np.min(y))
        maxX = max(maxX, np.max(x))
        minX = min(minX, np.min(x))
        
        plt.plot(x, y, c=color, label=name)
    print(maxY)
    plt.legend(loc=2)
    plt.xlim(minX, maxX)  
    plt.ylim(minY, maxY*10)
    plt.grid(True)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.yscale('log')
    print('hey')
    if savefigName != "":
        plt.savefig(savefigName)
    plt.close()