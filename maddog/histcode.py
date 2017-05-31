


import numpy as np


print 'Loading histcode.py'

global histData

def histData(data,fig_):

    ax = fig_

    ax.cla()
    data = np.random.rand(100)    
    ax.autoscale(True)
    ax.plot(data)

histogram_data = 0

def histogramGe(xdat,ydat):
    global histogram_data
    
    datout = np.random.rand(len(ydat))    
    if xdat!=None:
        print "runnign histogramGe: %s"%xdat[:8]
   	
    if ydat!=None:
        print "runnign histogramGe: %s"%ydat[:8]
    return(datout)
