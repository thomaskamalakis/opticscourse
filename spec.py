#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:00:28 2020

@author: thomas
"""

import numpy as np
import matplotlib.pyplot as plt

def gaussPulse(t, Pmax, tau):
    
    t0 = tau / 2.0 / np.sqrt( np.log(2.0) )
    return np.sqrt(Pmax) * np.exp( -t **2.0 /2.0 / t0**2.0 )

def squarePulse(t, Pmax, tau):
    
    p = np.zeros(t.size)
    
    for i, t1 in enumerate(t):
        if np.abs(t1) <= tau/2.0:
           p[ i ] = np.sqrt(Pmax)
           
    return p

def gaussPulseSpec(f, Pmax, tau):
    
    t0 = tau / 2.0 / np.sqrt( np.log(2.0) )
    return np.sqrt(Pmax) * t0 * np.sqrt(2.0*np.pi) *      \
           np.exp( -f**2.0 * 2.0 * np.pi**2.0 * t0**2.0)

def spec(t, y):
    Dt = t[1] - t[0]
    Df = 1.0 / (Dt * Nt)
    f = np.arange( -Nt/2.0, Nt/2.0, 1) * Df
    Y = np.fft.fftshift( np.fft.fft ( np.fft.fftshift ( y ) ) ) * Dt
    return f, Y
    
    
T = 2.0e-9
Tmin = -T/2.0
Tmax = T/2.0
Nt = 1024
Dt = T / Nt
tau = 100e-12
Pmax = 1

t = np.arange(Tmin, Tmax, Dt)
y = gaussPulse(t, Pmax, tau)
z = squarePulse(t, Pmax, tau)

f, Y = spec(t, y)
f, Z = spec(t, z)

Ytheory = gaussPulseSpec(f, Pmax, tau)

plt.close('all')
plt.figure(1)
plt.plot(t/tau, np.abs(y) ** 2.0 )
plt.xlabel('$t / \tau$')
plt.ylabel('$y(t) [\sqrt{Watt}]$')
plt.title('Initial Gaussian Pulse')

plt.figure(2)
plt.plot(f/1e9, np.abs(Y) ** 2.0,'o' )
plt.plot(f/1e9, np.abs(Ytheory) ** 2.0 )
plt.xlabel('$f$ [GHz] ')
plt.ylabel('$Y(f)$')
plt.title('Spectrum of Gaussian Pulse')
