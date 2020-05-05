#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:00:28 2020

@author: thomas
"""

import numpy as np
import matplotlib.pyplot as plt  
from liboptics import gaussPulse, width, propDispersion

def bitIndex(t, Tb, Nb):

    m = np.zeros( t.size )
    
    for i, t1 in enumerate(t):
        if (t1 >= 0) and (t1 < Nb*Tb):
            m[i] = np.floor( t1/ Tb )
        else:
            m[i] = -1
        
    return m.astype(int)

def bitPulses(t, bits, Tb, Nb, Pmax):

    x = np.zeros(t.size)
    m = bitIndex(t, Tb, Nb)    

    for i, mm in enumerate(m):
        if mm >= 0:    
            x[i] = bits[mm]
            
    return x * np.sqrt(Pmax)

bits = [1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1]
Nb = len(bits)
Rb = 10e9
Tb = 1.0 / Rb
Tg = 5.0 * Tb
Pmax = 0.01

T = Nb * Tb + 2.0 * Tg
Nt = 16384  
Tmin = -Tg
Tmax = Nb * Tb + Tg
Dt = T / Nt

t = np.arange(Tmin, Tmax, Dt)
x = bitPulses(t, bits, Tb, Nb, Pmax)

plt.close('all')   
plt.figure(1)
plt.plot(t, x)
   


