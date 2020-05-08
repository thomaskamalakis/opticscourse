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

def eyeOpening(p, highThreshold = 0.5, lowThreshold = 0.5):

    Nw, points = p.shape
    
    p = np.abs(p)
    highThreshold = highThreshold * np.max(p)
    lowThreshold = lowThreshold * np.max(p)
    im = np.floor(points / 2.0)
    im = int(im)
    
    highLevel = np.max(p)
    lowLevel = np.min(p)
    
    for i in range(0, Nw):
        
        level = p[i,im]
        
        if level > highThreshold and level < highLevel:
            highLevel = level
        elif level < lowThreshold and level > lowLevel:
            lowLevel = level
        
    return highLevel - lowLevel, highLevel, lowLevel, im

bits = np.random.randint(0, 2, 100)
Nb = len(bits)
Rb = 10e9
Tb = 1.0 / Rb
Tg = 10.0 * Tb
Pmax = 0.01
B = 2.0 * Rb
s2 = 1.0e-5

T = Nb * Tb + 2.0 * Tg
Nt = 16384  
Tmin = -Tg
Tmax = Nb * Tb + Tg
Dt = T / Nt

t = np.arange(Tmin, Tmax, Dt)
x = bitPulsesGaussian(t, bits, Tb, Nb, Pmax, B)

plt.close('all')   

tpx, px = eyeDiagram(t, x, Tb/2.0, Nb*Tb + Tb/2.0, 2.0*Tb )

y = addNoise(x, s2)
tpy, py = eyeDiagram(t, y, Tb/2.0, Nb*Tb + Tb/2.0, 2.0*Tb )

eyeX, hX, lX, imX = eyeOpening(px)
eyeY, hY, lY, imY = eyeOpening(py)
tmY = tpy[imY]

plotEyeDiagram(tpx,px)
plotEyeDiagram(tpy,py)
plt.plot(tmY,hY,'rs')
plt.plot(tmY,lY,'rs')


print('initial eye opening :', eyeX)
print('final eye opening :', eyeY)
    