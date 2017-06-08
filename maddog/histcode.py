


import numpy as np


print 'Loading histcode.py'

global histData

def histData(data,fig_):

    ax = fig_

    ax.cla()
    data = np.random.rand(100)    
    ax.autoscale(True)
    ax.plot(data)

histogram_data = None

def histogramGe(xdat,ydat):
    global histogram_data
    nbins = 100



    nints = len(ydat)


    pds = np.zeros(nints/2)
    tds = np.zeros(nints/2)

    intdat = np.array(ydat).astype(int)

    for i in range(0,nints,2):
        quad = (intdat[i] & 0x60000000) >> 29;
        chipnum = (intdat[i] & 0x18000000) >> 27;
        chan = (intdat[i] & 0x07C00000) >> 22;
        
        
        pd = (intdat[i] & 0xFFF);
        td = (intdat[i] & 0x3FF000) >> 12; 
        
        pds[i/2]=pd
        tds[i/2] = td
        
        ts = (intdat[i+1] & 0x1FFFFFFF);


    #hist(pds)

    #datout = np.random.rand(len(ydat))    
    if histogram_data == None:
    	histogram_data = np.zeros(nbins)

    (hd, edge)=np.histogram(pds,bins=nbins)
    histogram_data = histogram_data + hd

    return(edge[:-1], histogram_data )





