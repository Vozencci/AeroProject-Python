# REMARQUE: vz_ta, vx_ta, z_ta, x_ta ---------> méthode NUM
# REMARQUE: vz_tb, vx_tb, z_tb, x_tb ---------> méthode PFD

########## Add Lvzb, Lvxb and Lvza, Lvxa

import math
import statistics
import numpy as np
import matplotlib.pyplot as plt
from math import log10


def Chute(x_0, z_0, v_0, α, dt, n):
    
    
    g = 10
    
    
    vz_ta = v_0 * math.sin(α)
    vx_ta = v_0 * math.cos(α)
    z_ta = z_0
    x_ta = x_0
    
    vz_tb = v_0 * math.sin(α)
    vx_tb = v_0 * math.cos(α)
    z_tb = z_0
    x_tb = x_0
    
    
    t = 0
    
    
    L_vzb=[]
    L_vzb.append([ t , vz_tb ])
   
    L_vxb = []
    L_vxb.append([ t , vx_tb ])    
        
    L_zb=[]
    L_zb.append([ t , z_tb ])
    
    L_xb = []
    L_xb.append([ t , x_tb ])




    L_vza=[]
    L_vza.append([ t , vz_ta ])
    
    L_vxa = []
    L_vxa.append([ t , vx_ta ])
    
    L_za=[]
    L_za.append([ t , z_ta ])
    
    L_xa = []
    L_xa.append([ t , x_ta ])



    L = []
    LL = []


    while 0.5 * (z_tb + z_ta) > 0:
        
        # Chronophotographie
        
        t += dt


        # PFD
        
        vz_tb = - g * t + v_0 * math.sin(α)
        z_tb = - 0.5 * g * (t ** 2) + v_0 * math.sin(α) * t + z_0
            
        vx_tb = v_0 * math.cos(α)
        x_tb = v_0 * math.cos(α) * t + x_0


        # NUM
        
        vz_ta_dt = vz_ta - g * dt
        z_ta_dt = z_ta + dt * vz_ta

        vz_ta = vz_ta_dt
        z_ta = z_ta_dt
        
        
        vx_ta_dt = vx_ta
        x_ta_dt = x_ta + dt * vx_ta
        
        vx_ta = vx_ta_dt
        x_ta = x_ta_dt
        
        
        L_vzb.append([ t , vz_tb ])
        L_vxb.append([t , vx_tb])
        L_zb.append([ t , z_tb ])
        L_xb.append([t , x_tb])

        L_vza.append([ t , vz_ta ])
        L_vxa.append([ t , vx_ta])
        L_za.append([ t , z_ta ])
        L_xa.append([ t , x_ta])


    M_vzb = np.array(L_vzb) # martice de [ t , vz_tb ]
    M_vza = np.array(L_vza) # martice de [ t , vz_ta ]
    M_zb = np.array(L_zb) # martice de [ t , z_tb ]
    M_za = np.array(L_za) # martice de [ t , z_ta ]
    
    M_vxb = np.array(L_vxb) # martice de [ t , vx_tb ]
    M_vxa = np.array(L_vxa) # martice de [ t , vx_ta ]
    M_xb = np.array(L_xb) # martice de [ t , x_tb ]
    M_xa = np.array(L_xa) # martice de [ t , x_ta ]
            
    
    # plot creation (graph)

    # plot ( t , vz(t) )

    plt.plot( M_vza[ : , 0 ] , M_vza[ : , 1 ], color='r', label='num')
    plt.plot( M_vzb[ : , 0 ] , M_vzb[ : , 1 ], color='g', label='pfd')
    plt.axis([0, 1.1*t, z_ta, np.max(M_vza[ : , 1 ])*1.1])
    plt.xlabel("temps t (en s)")
    plt.ylabel("vitesse vz(t) (en m)")
    plt.title("Equation horaire de la vitesse vz(t) d'un objet à l'instant t")
    plt.show()
    
    # plot ( t , vx(t) )

    plt.plot( M_vxa[ : , 0 ] , M_vxa[ : , 1 ], label='num')
    plt.plot( M_vxb[ : , 0 ] , M_vxb[ : , 1 ], label='pfd')
    plt.axis([0, 1.1*t, 0, np.max(M_vxa[ : , 1 ])*1.1])
    plt.xlabel("temps t (en s)")
    plt.ylabel("vitesse vx(t) (en m)")
    plt.title("Equation horaire de la vitesse vx(t) d'un objet à l'instant t")
    plt.show()
    
    # plot ( t , z(t) )

    plt.plot( M_za[ : , 0 ] , M_za[ : , 1 ], color='r', label='num')
    plt.plot( M_zb[ : , 0 ] , M_zb[ : , 1 ], color='g', label='pfd')
    plt.axis([0, 1.1*t, z_ta, np.max(M_za[ : , 1 ])*1.1])
    plt.xlabel("temps t (en s)")
    plt.ylabel("position z(t) (en m)")
    plt.title("Equation horaire de la position z(t) d'un objet à l'instant t")
    plt.show()
    
    # plot ( t , x(t) )

    plt.plot( M_xa[ : , 0 ] , M_xa[ : , 1 ], label='num')
    plt.plot( M_xb[ : , 0 ] , M_xb[ : , 1 ], label='pfd')
    plt.axis([0, 1.1*t, 0, np.max(M_xa[ : , 1 ])*1.1])
    plt.xlabel("temps t (en s)")
    plt.ylabel("position x(t) (en m)")
    plt.title("Equation horaire de la position x(t) d'un objet à l'instant t")
    plt.show()
    
    
    # Calcul de l'erreur relative E_n
    
    # Méthode 1: Continu
    
    E_n = abs(M_zb - M_za)
    print("L'erreur relative E(n) = " + str(statistics.mean( E_n[ : , 1 ] )) + " via la méthode Continue")
    
    
    # Methode 2: Discrete

    """for k in range(1, n+1):
        
        t = 0 
        dt = 1/k
            
        
        v_0 = 0
        g = 10
    
    
        v_t = v_0
        z_t = z_0
        

        while t < 1:
            
            t = t + dt
    
            v_t_dt = v_t - g * dt
            z_t_dt = z_t + dt * v_t
        
            v_t = v_t_dt
            z_t = z_t_dt
            
                        
        L.append([k, abs(z_t - (- 0.5 * g + z_0))])
        
        LL.append([log10(k), log10(abs(z_t - (- 0.5 * g + z_0)))])"""
        
    for k in range(1, n+1):
            
        t = 0 
        dt = 1/k
                
        g = 10
        
        vz_ta = v_0
        z_ta = z_0

        while t < 1:
                
            t = t + dt
        
            vz_ta_dt = vz_ta - g * dt
            z_ta_dt = z_ta + dt * vz_ta

            vz_ta = vz_ta_dt
            z_ta = z_ta_dt
                
                            
        L.append([k, abs(z_ta - (- 0.5 * g + v_0 * math.sin(α) + z_0))])
            
        LL.append([log10(k), log10(abs(z_ta - (- 0.5 * g + v_0 * math.sin(α) + z_0)))])
        
        
    M = np.array(L)    
    
    plt.plot( M[ : , 0 ] , M[ : , 1 ], color='r')
    plt.axis([-10, 110, -10, 10])
    plt.xlabel("n")
    plt.ylabel("E(n)")
    plt.title("Erreur relative")
    plt.show()
    
    
    MM = np.array(LL)
    
    plt.plot( MM[ : , 0 ] , MM[ : , 1 ], color='b')
    plt.axis([-log10(10), log10(1100), -log10(1000), log10(100)])
    plt.xlabel("log(n)")
    plt.ylabel("log(E(n))")
    plt.title("Erreur relative Log")
    plt.show()