#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created by Sarmeegan SABESAN aka. Vozencci.

The following function is the same as the procedure FreeFallDFP. This function will be called for the computation
of the relative error...
"""

import numpy as np

def FreeFallDFP():
    
    v_0 = 0
    z_0 = float(input("z_0 = "))
    g = 10
    t = 0
    dt = float(input("dt = "))
    v_t = v_0
    z_t = z_0
    
    L = []
    
    while z_t > 0:
        
        v_t = - g * t
        z_t = - 0.5 * g * (t ** 2) + z_0
        t += dt
        
        L.append([v_t , z_t])
        
    print("Total measured couple [ v(t) , z(t) ] number is: " + str(len(L)))
    return(np.array(L))