#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:00:28 2020

@author: thomas
"""

import numpy as np
import matplotlib.pyplot as plt  
from liboptics import gaussPulse, squarePulse, spec, squarePulseSpec, width

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

b = width(t, y, useInterp=True)

print(b/tau)

