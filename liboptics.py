#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 06:30:48 2020

@author: thomas
"""

import numpy as np

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
           
def squarePulseSpec(f, Pmax, tau):
    
    return np.sinc(f*tau) * tau * np.sqrt(Pmax)

def spec(t, y):
    Dt = t[1] - t[0]
    Nt = t.size    
    Df = 1.0 / (Dt * Nt)
    f = np.arange( -Nt/2.0, Nt/2.0, 1) * Df
    Y = np.fft.fftshift( np.fft.fft ( np.fft.fftshift ( y ) ) ) * Dt
    return f, Y

def width(t, y, useInterp = False):
    
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
    
    if foundright:      
       if useInterp:
           ts = np.array([t[i-1], t[i]])
           ps = np.array([p[i-1], p[i]])
           bright = np.interp(0.5*pmax, ps, ts)
       else:
           bright = t[i]

       bright = bright - t[imax]
       
    i = imax
            
    while (not foundleft) and (i>=0):
        if  p[i] <= 0.5 * pmax:
            foundleft = True
            bleft = t[imax] - t[i]
        else:        
            i = i-1
    
    if foundleft:
       if useInterp:
           ts = np.array([t[i], t[i+1]])
           ps = np.array([p[i], p[i+1]])
           bleft = np.interp(0.5*pmax, ps, ts)
       else:
           bleft = t[i]
           
       bleft = t[imax] - bleft  
        
    if (bright is not None) and (bleft is not None):
        b = bright + bleft
    else:
        b = None
    
    return b

def invspec(f, Y):
    Df = f[1] - f[0]
    Nf = f.size    
    Dt = 1.0 / (Df * Nf)
    t = np.arange( -Nf/2.0, Nf/2.0, 1) * Dt
    y = np.fft.fftshift( np.fft.ifft ( np.fft.fftshift ( Y ) ) ) / Dt
    return t, y

def propDispersion(t, y, b2, L):
    
    f, Y = spec(t, y)
    di = np.exp( 1j * f ** 2.0 * b2 * L / 2.0 )
    Z = Y * di
    _ , z = invspec(f, Z)
    return z 