#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created by Sarmeegan SABESAN aka. Vozencci.

The following function is the same as the procedure FreeFallDFP. This function will be called for the computation
of the relative error...
"""

def FreeFallDFP():
    
    v_0 = 0
    z_0 = float(input("z_0 = "))
    g = 10
    t = 0
    dt = float(input("dt = "))
    v_t = v_0
    z_t = z_0
    
    while z_t > 0:
        
        v_t = - g * t
        z_t = - 0.5 * g * (t ** 2) + z_0
        t += dt
        
        print("( v(t) , z(t) ) =  ( " +str(v_t)+ " , " +str(z_t)+ " )")
        
    return (v_t, z_t)