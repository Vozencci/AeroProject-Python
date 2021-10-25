#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created by Sarmeegan SABESAN aka. Vozencci.

The following code will enable us to compute the relative error between the two modelisation of a falling object.
Two different methods will be applied.
The first one is the conventionnal method using a time loop.
The second one, more implicit, will be using a time mesh where at a t_max instant, we will cut the interval [0,t_max]
with regular spacings n.
"""


from FreeFall_Function import FreeFall
from FreeFallDFP_Function import FreeFallDFP

### Method 1: Time Loop ###

def TimeLoop():
    m = min(len(FreeFall()) , len(FreeFallDFP()))
    print("Common minimum measurement number is: " + str(m))
    print(abs(FreeFall()[ : m + 1] - FreeFallDFP()[1 : m + 1]))








### Method 2: Time Mesh ### (UNDER HEAVY DEVELOPMENT)

"""

def TimeMesh():
    n = input("iteration number n = ")
    t_max = 1
    dt = 1/n
    
    
"""