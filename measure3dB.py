#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:00:28 2020

@author: thomas
"""

import numpy as np
import matplotlib.pyplot as plt  
from liboptics import gaussPulse, squarePulse, spec, squarePulseSpec

def width(t, y):
    
    p = np.abs(y) ** 2.0
    pmax = np.max(p)
    imax = np.argmax( p )
    
    foundright = False
    foundleft = False
    
    i = imax
    bright = None
    bleft = None
    
    while (not foundright) and (i < p.size):
        if p[i] <= 0.5 * pmax:
            foundright = True
            bright = t[i] - t[imax]
        else:       
            i = i+1
    
    iright = i    
    i = imax
            
    while (not foundleft) and (i>=0):
        if  p[i] <= 0.5 * pmax:
            foundleft = True
            bleft = t[imax] - t[i]
        else:        
            i = i-1
        
    ileft = i

    
    if (bright is not None) and (bleft is not None):
        b = bright + bleft
    else:
        b = None
    
    return b, foundright, foundleft, bright, bleft, iright, ileft       
    
T = 2.0e-9
Tmin = -T/2.0
Tmax = T/2.0
Nt = 1024
Dt = T / Nt
tau = 100e-12
Pmax = 1

t = np.arange(Tmin, Tmax, Dt)
y = gaussPulse(t, Pmax, tau)

plt.close('all')
plt.figure(1)
plt.plot(t/tau, np.abs(y) ** 2.0, 's', label = 'Gauss' )
plt.xlabel('t / tau')
plt.ylabel('Pulse Power [Watt]')
plt.title('Initial Pulses')
plt.legend()

b, foundright, foundleft, bright, bleft, iright, ileft = width(t, y)

plt.plot(t[ileft]/ tau, np.abs(y[ileft]) ** 2.0, 'o')
plt.plot(t[iright]/ tau, np.abs(y[iright]) ** 2.0, 'o')


