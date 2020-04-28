#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:00:28 2020

@author: thomas
"""

import numpy as np
import matplotlib.pyplot as plt  
from liboptics import gaussPulse, width, propDispersion
    
T = 2.0e-10
Tmin = -T/2.0
Tmax = T/2.0
Nt = 1024
Dt = T / Nt
tau = 20e-12
Pmax = 1
b2 = 20 * 1e-27
L = 100 * 1e3

t = np.arange(Tmin, Tmax, Dt)
y = gaussPulse(t, Pmax, tau)

b = width(t, y, useInterp=True)
z = propDispersion(t, y, b2, L)

plt.close('all')
plt.figure(1)
plt.plot(t/1e-12,np.abs(y) ** 2.0, label ='Input')
plt.plot(t/1e-12,np.abs(z) ** 2.0, label ='Output')
plt.xlabel('t / tau')
plt.ylabel('Pulse Power [Watt]')
plt.legend()

bout = width(t, z, useInterp=True)
print(bout/b)

