#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created by Sarmeegan SABESAN aka. Vozencci.

The following function is the same as the procedure FreeFall. This function will be called for the computation
of the relative error...
"""

import numpy as np

def FreeFall():
    
    v_0 = 0
    z_0 = float(input("z_0 = "))
    g = 10
    dt = float(input("dt = "))
    v_t = v_0
    z_t = z_0
    
    L = []
    
    while z_t > 0:
        
            v_t_dt = v_t - g * dt
            z_t_dt = z_t + dt * v_t
            
            v_t = v_t_dt
            z_t = z_t_dt
            
            L.append([v_t , z_t])
            
    
    print("Total measured couple [ v(t) , z(t) ] number is: " + str(len(L)))
    return(np.array(L))