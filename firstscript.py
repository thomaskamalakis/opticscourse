#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:00:28 2020

@author: thomas
"""

import numpy as np
import matplotlib.pyplot as plt

def gaussPulse(t, Pmax, tau):
    
    t0 = tau / 2.0 / np.sqrt( np.log(2) )
    return np.sqrt(Pmax) * np.exp( -t **2.0 /2.0 / t0**2.0 )

def squarePulse(t, Pmax, tau):
    
    p = np.zeros(t.size)
    
    for i, t1 in enumerate(t):
        if np.abs(t1) <= tau/2.0:
           p[ i ] = np.sqrt(Pmax)
           
    return p
        
T = 2.0e-9
Tmin = -T/2.0
Tmax = T/2.0
Nt = 1024
Dt = T / Nt
tau = 100e-12
Pmax = 1

t = np.arange(Tmin, Tmax, Dt)
y = gaussPulse(t, Pmax, tau)
z = squarePulse(t, Pmax, tau )

plt.close('all')
plt.figure(1)
plt.plot(t/tau, np.abs(y) ** 2.0 )
plt.plot(t/tau, np.abs(z) ** 2.0 )

plt.xlabel('$t / \tau$')
plt.ylabel('$y(t) [\sqrt{Watt}]$')
plt.title('Initial Gaussian Pulse')