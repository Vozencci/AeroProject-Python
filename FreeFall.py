#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created by Sarmeegan SABESAN aka. Vozencci.

The following code is a modelisation of a falling object due to gravity from a certain height z_0.
Note that aerodynamic forces such as Drag and Lift forces aren't taken into account.
Note that the object has been dropped without an initial speed or an initial angle.

The idea of such a construction lies on the incremental construction according to the finite
difference method.
"""

### Initial conditions (t=0s) ###

v_0 = 0
z_0 = float(input("z_0 = "))

### Known parameters ###

g = 10

### Incrementer ###

dt = float(input("dt = "))

### Dynamic variables ###

# (notation)

"v(t + dt) == v_t_dt"
"v(t) == v_t"

"z(t + dt) == z_t_dt"
"z(t) == z_t"

# first values (incremental method)

v_t = v_0
z_t = z_0

print("( v(t) , z(t) ) =  ( " +str(v_t)+ " , " +str(z_t)+ " )")

# finite difference method application (EXPLICIT METHOD)

while z_t > 0:
        
        v_t_dt = v_t - g * dt
        z_t_dt = z_t + dt * v_t
        
        v_t = v_t_dt
        z_t = z_t_dt
        
        print("( v(t) , z(t) ) =  ( " +str(v_t)+ " , " +str(z_t)+ " )")
        
        # MAKE A PLOT