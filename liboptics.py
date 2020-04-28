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

