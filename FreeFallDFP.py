#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created by Sarmeegan SABESAN aka. Vozencci.

The following code is a modelisation of a falling object due to gravity from a certain height z_0.
Note that aerodynamic forces such as Drag and Lift forces aren't taken into account.
Note that the object has been dropped without an initial speed or an initial angle.

Basic method will be applied here, meaning we know the analytic solution to the object's motion equation.
"""

### Initial conditions (t=0s) ###

v_0 = 0
z_0 = float(input("z_0 = "))

### Known parameters ###

g = 10

### Incrementer ###

t = 0
dt = float(input("dt = "))

### Dynamic variables ###

# (notation)

"v(t) == v_t"
"z(t) == z_t"

# first values (incremental method)

v_t = v_0
z_t = z_0

# Solutions of the object's motion equation (DFP)

while z_t > 0:
    
    v_t = - g * t
    z_t = - 0.5 * g * (t ** 2) + z_0
    t += dt
    
    print("( v(t) , z(t) ) =  ( " +str(v_t)+ " , " +str(z_t)+ " )")
    
    # MAKE A PLOT