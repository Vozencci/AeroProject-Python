# REMARQUE: Methode 100% NUM

import math
import numpy as np
import matplotlib.pyplot as plt

print("Executer Vol( x(0), z(0) , C , dt )")

def Vol(x_0, z_0, C, dt):
    
    
    g = 10
    rhô = 1.2 # air (usi)
    m = 0.005 # Pour un avion en papier (usi)
    S = 0.02 # Pour un avion en papier (usi)
    Cx = 0.07 # Pour un avion en papier (usi)
    Cp = 1 # Pour un avion en papier (usi)
    f = Cp/Cx
    print(f)
    alpha = math.atan(1/f) # Inverse de la finesse f (usi)
    
    
    """Variation du paramètre de la vitesse initiale:"""
    
    v_0_PFS = math.sqrt((2 * m * g * math.cos(alpha)) / (rhô * S * Cp))
    v_0 = C * v_0_PFS
    
    vz_t = - v_0 * math.sin(alpha)
    vx_t = v_0 * math.cos(alpha)
    z_t = z_0
    x_t = x_0
    
    
    t = 0
    
    
    Lz = []
    Lz.append([t, z_t])
    
    Lvz = []
    Lvz.append([t, vz_t])
    
    
    
    Lx = []
    Lx.append([t, x_t])
    
    Lvx = []
    Lvx.append([t, vx_t])
    
    
    L_trajectoire = []
    L_trajectoire.append([x_t, z_t])


    
    while z_t > 0:
        
        
        # Chronophotographie
        
        t += dt
        
        
        # Discrétisation sur z
        
        U = math.sqrt(vx_t ** 2 + vz_t ** 2)
        
        Fz_t = - g - (0.5 / m) * Cx * rhô * S * U * vz_t + (0.5 / m) * Cp * rhô * S * U * vx_t
        
        vz_t_dt = vz_t + dt * Fz_t
        z_t_dt = z_t + dt * vz_t
            
    
        
        # Discrétisation sur x
        
        U = math.sqrt(vx_t ** 2 + vz_t ** 2)
        
        Fx_t = - (0.5 / m) * Cx * rhô * S * U * vx_t - (0.5 / m) * Cp * rhô * S * U * vz_t
    
        vx_t_dt = vx_t + dt * Fx_t
        x_t_dt = x_t + dt * vx_t
        
        
        # Itérations
        
        vz_t = vz_t_dt
        z_t = z_t_dt
        
        vx_t = vx_t_dt
        x_t = x_t_dt
        
        
        # Listes
        
        Lz.append([ t , z_t ])
        Lvz.append([ t , vz_t ])
        
        Lx.append([ t , x_t ])
        Lvx.append([ t , vx_t ])
        
        L_trajectoire.append([ x_t , z_t ])
    
    
    # Matrices
    
    Mz = np.array(Lz)
    Mvz = np.array(Lvz)
    
    Mx = np.array(Lx)
    Mvx = np.array(Lvx)
    
    M_trajectoire = np.array(L_trajectoire)


    # Plot 1: [ t , z_t ]

    plt.plot( Mz[ : , 0 ] , Mz[ : , 1 ], color='r', label='num')
    plt.axis([0,25,0,5])
    plt.xlabel("temps t (en s)")
    plt.ylabel("position z(t) (en m)")
    plt.title("Equation horaire de la position z(t) d'un objet a l'instant t")
    plt.show()
    
    
    # Plot 2: [ t , x_t ]

    plt.plot( Mx[ : , 0 ] , Mx[ : , 1 ], color='g', label='num')
    plt.axis([-1,15,-1,25])
    plt.xlabel("temps t (en s)")
    plt.ylabel("position x(t) (en m)")
    plt.title("Equation horaire de la position x(t) d'un objet a l'instant t")
    plt.show()
    

    # Plot 3: [ t , vz_t ]

    plt.plot( Mvz[ : , 0 ] , Mvz[ : , 1 ], color='b', label='num')
    plt.axis([-1,10,-10,10])
    plt.xlabel("temps t (en s)")
    plt.ylabel("vitesse v_z(t) (en m)")
    plt.title("Equation horaire de la vitesse v_z(t) d'un objet a l'instant t")
    plt.show()
    
    
    # Plot 4: [ t , vx_t ]

    plt.plot( Mvx[ : , 0 ] , Mvx[ : , 1 ], color='m', label='num')
    plt.axis([-1,10,-10,10])
    plt.xlabel("temps t (en s)")
    plt.ylabel("vitesse v_x(t) (en m)")
    plt.title("Equation horaire de la vitesse v_x(t) d'un objet a l'instant t")
    plt.show()
    
    
    # Plot 5: equation de la trajectoire [ x_t , z_t ]
    
    plt.plot( M_trajectoire[ : , 0 ] , M_trajectoire[ : , 1 ], color='k', label='num')
    plt.axis([0,30,0,5])
    plt.xlabel("position x(t) (en m)")
    plt.ylabel("position z(x) (en m)")
    plt.title("Equation de la trajectoire")
    plt.show()