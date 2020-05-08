#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:00:28 2020

@author: thomas
"""

import numpy as np
import matplotlib.pyplot as plt  
from liboptics import bitPulsesGaussian 

def eyeDiagram(t, x, tstart, tend, tduration):
    
    x = np.abs(x)
    Dt = t[1] - t[0]
    
    N = (tend - tstart) / tduration
    N = np.floor(N)
    N = int(N)
    
    nDuration = np.round(tduration / Dt)
    nDuration = int(nDuration)
    indmin = np.argmin( np.abs(t-tstart) )
    indmax = np.argmin( np.abs(t-tend) )

    i = indmin
    
    xpattern = np.zeros([N, nDuration])
    tpattern = np.arange(0, nDuration) * Dt
    
    count = 0
    
    while i + nDuration <= indmax:
        
        s = x[ i:i+nDuration ]
        xpattern[count, :] = s
        count += 1
        i += nDuration
        
    return tpattern, xpattern

def plotEyeDiagram(t, p):
    
    plt.figure()
    
    N, points = p.shape
    
    for i in range(0, N):
        s = p[i, :]
        plt.plot(t, s, 'bo')

def addNoise(x, s2):
    
    x = x + np.sqrt(s2) * np.random.randn(x.size)
    return x
    
bits = [1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1]
Nb = len(bits)
Rb = 10e9
Tb = 1.0 / Rb
Tg = 10.0 * Tb
Pmax = 0.01
B = 2.0 * Rb
s2 = 5.0e-4

T = Nb * Tb + 2.0 * Tg
Nt = 16384  
Tmin = -Tg
Tmax = Nb * Tb + Tg
Dt = T / Nt

t = np.arange(Tmin, Tmax, Dt)
x = bitPulsesGaussian(t, bits, Tb, Nb, Pmax, B)

plt.close('all')   
plt.figure(1)
plt.plot(t, np.abs(x) )

tpx, px = eyeDiagram(t, x, Tb/2.0, Nb*Tb + Tb/2.0, 2.0*Tb )
plotEyeDiagram(tpx,px)

y = addNoise(x, s2)

plt.figure()
plt.plot(t, np.abs(y) )

tpy, py= eyeDiagram(t, y, Tb/2.0, Nb*Tb + Tb/2.0, 2.0*Tb )
plotEyeDiagram(tpy,py)
