# REMARQUE: vz_ta, vx_ta, z_ta, x_ta ---------> méthode NUM
# REMARQUE: vz_tb, vx_tb, z_tb, x_tb ---------> méthode PFD

import math
import statistics
import numpy as np
import matplotlib.pyplot as plt
from math import log10


def Lancer(x_0, z_0, v_0, α, dt):
    
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
    
    Lb=[]
    Lb.append([ t , z_tb ])
    
    L1b = []
    L1b.append([ t , x_tb ])

    
    La=[]
    La.append([ t , z_ta ])
    
    L1a = []
    L1a.append([ t , x_ta ])

    while 0.5 * (z_tb + z_ta) > 0:
        
        # Chronophotographie
        
        t += dt


        # PFD
        
        vz_tb = - g * t + vz_tb
        z_tb = - 0.5 * g * (t ** 2) + vz_tb * t + z_0
            
        vx_tb = vx_tb
        x_tb = vx_tb * t + x_0


        # NUM
        
        vz_ta_dt = vz_ta - g * dt
        z_ta_dt = z_ta + dt * vz_ta

        vz_ta = vz_ta_dt
        z_ta = z_ta_dt
        
        
        vx_ta_dt = vx_ta
        x_ta_dt = x_ta + dt * vx_ta
        
        vx_ta = vx_ta_dt
        x_ta = x_ta_dt
        
        
        
        Lb.append([ t , z_tb ])
        L1b.append([t , x_tb])
            
        La.append([ t , z_ta ])
        L1a.append([ t , x_ta])
    
    Mb = np.array(Lb) # martice de [ t , z_tb ]
    Ma = np.array(La) # martice de [ t , z_ta ]
    
    M1b = np.array(L1b) # martice de [ t , x_tb ]
    M1a = np.array(L1a) # martice de [ t , x_ta ]
            
    # plot creation (graph)


    # plot ( t , z(t) )

    plt.plot( Ma[ : , 0 ] , Ma[ : , 1 ], color='r', label='num')
    plt.plot( Mb[ : , 0 ] , Mb[ : , 1 ], color='g', label='pfd')
    plt.axis([0, 1.1*t, z_ta, z_0*1.1])
    plt.xlabel("temps t (en s)")
    plt.ylabel("position z(t) (en m)")
    plt.title("Equation horaire de la position z(t) d'un objet à l'instant t")
    plt.show()

    
    # plot ( t , x(t) )

    plt.plot( M1a[ : , 0 ] , M1a[ : , 1 ], label='num')
    plt.plot( M1b[ : , 0 ] , M1b[ : , 1 ], label='pfd')
    plt.axis([0, 1.1*t, x_ta, x_0*1.1])
    plt.xlabel("temps t (en s)")
    plt.ylabel("position x(t) (en m)")
    plt.title("Equation horaire de la position x(t) d'un objet à l'instant t")
    plt.show()


    print("Test Vérification...")
 
    print("Nombre total de couple [ t , z(t) ] mesuré pour la méthode NUM: " + str(len(La)))
    print("Nombre total de couple [ t , z(t) ] mesuré pour la méthode PFD: " + str(len(Lb)))
 
    print("Nombre total de couple [ v(t) , z(t) ] mesuré pour la méthode NUM: " + str(len(L1a)))
    print("Nombre total de couple [ v(t) , z(t) ] mesuré pour la méthode PFD: " + str(len(L1b)))
    
    
    # Calcul de l'erreur relative E_n
    # Méthode 1: Continu
    
    E_n = abs(Mb - Ma)
    print("L'erreur relative E(n) = " + str(statistics.mean( E_n[ : , 1 ] )) + " via la méthode Continue")
    
    
    return(np.array(La), np.array(Lb), np.array(L1a), np.array(L1b))


# Erreur relative version discrètisé

def Erreur_Relative_Discrète(z_0, n):
    
    v_0 = 0    
    g = 10
    
    v_t = v_0
    z_t = z_0
        
    dt = 1/n
    t_max = 0

    while t_max < 1:
            
        t_max = t_max + dt
    
        v_t_dt = v_t - g * dt
        z_t_dt = z_t + dt * v_t
        
        v_t = v_t_dt
        z_t = z_t_dt
            
    print("L'Erreur relative E(n) = " + str(abs(z_t - (- 0.5 * g + z_0))) + " via la méthode Discrète" )
    

# Erreur relative version discrètisé et logarithmique

def Erreur_Relative_Discrète_Log(z_0, n): #PROBLEME#
    
    v_0 = 0
    g = 10
    
    v_t = v_0
    z_t = z_0
        
    dt = 1/n
    t_max = 0
    
    n = 0
    
    L = []

    while t_max < 1:
            
        t_max = t_max + dt
    
        v_t_dt = v_t - g * dt
        z_t_dt = z_t + dt * v_t
        
        v_t = v_t_dt
        z_t = z_t_dt
            
        E_n = log10(abs(z_t - (- 0.5 * g + z_0)))
        
        n += 1
        
        L.append([log10(n), E_n])
        
        
    M = np.array(L)
    
    
    # plot
    
    plt.plot( M[ : , 0 ] , M[ : , 1 ])
    plt.axis([-1, 5, -1.5, 1])
    plt.xlabel("log(n)")
    plt.ylabel("log(E(n))")
    plt.title("Graphe de log(E(n)) en fonction de log(n)")
    plt.show()