# REMARQUE: v_ta , z_ta ---------> méthode NUM
# REMARQUE: v_tb , z_tb ---------> méthode PFD

import statistics
import numpy as np
import matplotlib.pyplot as plt
from math import log10

def Chute(z_0, dt, n):
    
    v_0 = 0
    g = 10
    
    
    v_ta = v_0
    z_ta = z_0
    
    v_tb = v_0
    z_tb = z_0
    
    
    t = 0
    
    
    Lb=[]
    Lb.append([ t , z_tb ])
    
    L1b = []
    L1b.append([ t , v_tb ])

    
    La=[]
    La.append([ t , z_ta ])
    
    L1a = []
    L1a.append([ t , v_ta ])
    
    
    L = []
    LL = []


    while 0.5 * (z_tb + z_ta) > 0:
        
        # Chronophotographie
        
        t += dt


        # PFD
        
        v_tb = - g * t
        z_tb = - 0.5 * g * (t ** 2) + z_0


        # NUM
        
        v_t_dta = v_ta - g * dt
        z_t_dta = z_ta + dt * v_ta
            
        v_ta = v_t_dta
        z_ta = z_t_dta
        
        Lb.append([ t , z_tb ])
        L1b.append([ t , v_tb ])
            
        La.append([ t , z_ta ])
        L1a.append([ t , v_ta ])
    
    Mb = np.array(Lb) # martice de [ t , z_tb ]
    Ma = np.array(La) # martice de [ t , z_ta ]
    
    M1b = np.array(L1b) # martice de [ t , v_tb ]
    M1a = np.array(L1a) # martice de [ t , v_ta ]
            
    # plot creation (graph)


    # plot ( t , z(t) )

    plt.plot( Ma[ : , 0 ] , Ma[ : , 1 ], color='r', label='num')
    plt.plot( Mb[ : , 0 ] , Mb[ : , 1 ], color='g', label='pfd')
    plt.axis([0, 1.1*t, z_ta, z_0*1.1])
    plt.xlabel("temps t (en s)")
    plt.ylabel("position z(t) (en m)")
    plt.title("Equation horaire de la position z(t) d'un objet à l'instant t")
    plt.show()

    
    # plot ( z(t) , v(t) )

    plt.plot( M1a[ : , 0 ] , M1a[ : , 1 ], label='num')
    plt.plot( M1b[ : , 0 ] , M1b[ : , 1 ], label='pfd')
    plt.axis([0, 1.1*t, 1.1*v_tb, 0])
    plt.xlabel("temps t (en s)")
    plt.ylabel("vitesse v(t) (en m/s)")
    plt.title("Equation horaire de la vitesse v(t) d'un objet à l'instant t")
    plt.show()


    print("Test Vérification...")
 
    print("Nombre total de couple [ t , z(t) ] mesuré pour la méthode NUM: " + str(len(La)))
    print("Nombre total de couple [ t , z(t) ] mesuré pour la méthode PFD: " + str(len(Lb)))
 
    print("Nombre total de couple [ t , z(t) ] mesuré pour la méthode NUM: " + str(len(L1a)))
    print("Nombre total de couple [ t , z(t) ] mesuré pour la méthode PFD: " + str(len(L1b)))
    
    
    # Calcul de l'erreur relative E_n
    
    # Methode 1: Continu
    
    E_n = abs(Mb - Ma)
    print("L'erreur relative E(n) = " + str(statistics.mean( E_n[ : , 1 ] )) + " via la méthode Continue")
    
    
    # Methode 2: Discretise

    for k in range(1, n+1):
        
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
        
        LL.append([log10(k), log10(abs(z_t - (- 0.5 * g + z_0)))])
        
        
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
    
    
    return(np.array(La), np.array(Lb), np.array(L1a), np.array(L1b))