#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created by Sarmeegan SABESAN aka. Vozencci.

The following code is a modelisation of a falling object due to gravity from a certain height z_0.
In this case, however,the object has been launched with an initial velocity v_0 and an initial angle α.
Note that aerodynamic forces such as Drag and Lift forces aren't taken into account.

The idea of such a construction lies on the incremental construction according to the finite
difference method as shown in the previous example.
"""

# Plot instruments

import math
import numpy as np
import matplotlib.pyplot as plt

L1=[]
L2=[]

### Initial conditions (t=0s) ###

v_0 = float(input("v_0 = "))
z_0 = float(input("z_0 = "))
x_0 = float(input("x_0 = "))

### Known parameters ###

g = 10 #in m.s^-2
α = float(input("α = "))

### Incrementer ###

dt = float(input("dt = "))

### Dynamic variables ###

# (notation)

"v(t) == v_z(t) + v_x(t)"


"v_z(t + dt) == vz_t_dt"
"v_z(t) == vz_t"

"z(t + dt) == z_t_dt"
"z(t) == z_t"

"v_x(t + dt) == vx_t_dt"
"v_x(t) == vx_t"

"x(t + dt) == x_t_dt"
"x(t) == x_t"

# first values (incremental method)

v_0z = v_0 * math.sin(α)
v_0x = v_0 * math.cos(α)

vz_t = v_0z
vx_t = v_0x

z_t = z_0
x_t = x_0

print("( v_z(t) , z(t) , v_x(t) , x(t) ) =  ( " +str(vz_t)+ " , " +str(z_t)+ " , " +str(vx_t)+ " , " +str(x_t)+ " )")

# finite difference method application

while z_t > 0:
    
    vz_t_dt = vz_t - g * dt
    z_t_dt = z_t + dt * vz_t

    vz_t = vz_t_dt
    z_t = z_t_dt
    
    
    vx_t_dt = vx_t
    x_t_dt = x_t + dt * vx_t
    
    vx_t = vx_t_dt
    x_t = x_t_dt
    
    
    L1.append([ vz_t , z_t ]) # for the plot
    L2.append([ vx_t , x_t ]) # for the plot

    
    print("( v_z(t) , z(t) , v_x(t) , x(t) ) =  ( " +str(vz_t)+ " , " +str(z_t)+ " , " +str(vx_t)+ " , " +str(x_t)+ " )")

M1 = np.array(L1) # matrix of [ vz_t,z_t ]
M2 = np.array(L2) # matrix of [ vx_t,x_t ]

# plot creation (graph)

plt.plot( M1[ : , 0 ] , M1[ : , 1 ] )
plt.axis([vz_t, 10, z_t, 10])
plt.show()


plt.plot( M2[ : , 0 ] , M2[ : , 1 ] )
plt.axis([vx_t, 10, x_t, 10])
plt.show()