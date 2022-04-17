# REMARQUE: Methode 100% NUM

import math
import numpy as np
import matplotlib.pyplot as plt
from math import log10


print("### Données athmosphérique ###")
print("Accélération de la pesanteur: g = 10 m/s^2")
print("Masse volumique de l'air: rho = 1.2 Kg/m^3")
print("")
print("### Spec de l'avion ###")
print("Masse de l'avion: m = 0.009 Kg")
print("Surface totale de l'avion: S = 0.02 m^2")
print("")
print("### Code Vol Libre ###")
print("Executer Vol( x(0), z(0), v(0), Cx, Cp, alpha, dt, n )")

def Vol(x_0, z_0, v_0, Cx, Cp, alpha, dt, n):
    
    
    g = 10
    rho = 1.2 # air (usi)
    m = 0.009 # Pour un avion en papier (usi)
    S = 0.02 # Pour un avion en papier (usi)
    

    """Choix PFD ou PFS:"""
    
    print("### Choix du vol ###")
    print("")
    e = input("PFD ou PFS: ")
    
    if e == "PFS":
        
        Cx = (2*m*g*math.sin(alpha))/(rho*(v_0**2)*S) # Pour un avion en papier (usi)
        Cp = (2*m*g*math.cos(alpha))/(rho*(v_0**2)*S) # Pour un avion en papier (usi)
        f = Cp/Cx
        alpha = math.atan(1/f) # Inverse de la finesse f (usi)
        
        v_0_PFS = math.sqrt((2 * m * g * math.cos(alpha)) / (rho * S * Cp))
        v_0 = v_0_PFS
        
        print("finesse de l'avion: f = " + str(f))
        print("Coefficient de traînée de l'avion: Cx = " + str(Cx))
        print("Coefficient de portance de l'avion: Cp = " + str(Cp))
        print("Angle d'attaque de l'avion: alpha= " + str(alpha))
        print("Vitesse PFS de l'avion: v(0) = " + str(v_0))
        
    elif e == "PFD":
        
        None
        
    else: 
        
        return("Erreur, veuillez recommencer...")
    
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
    
    
    L = []
    LL = []



    while z_t > 0:
    
    
        # Chronophotographie
    
        t += dt
    
    
        # Discrétisation sur z
    
        U = math.sqrt(vx_t ** 2 + vz_t ** 2)
    
        Fz_t = - g - (0.5 / m) * Cx * rho * S * U * vz_t + (0.5 / m) * Cp * rho * S * U * vx_t
            
        vz_t_dt = vz_t + dt * Fz_t
        z_t_dt = z_t + dt * vz_t
    
    
    
        # Discrétisation sur x
        
        U = math.sqrt(vx_t ** 2 + vz_t ** 2)
        
        Fx_t = - (0.5 / m) * Cx * rho * S * U * vx_t - (0.5 / m) * Cp * rho * S * U * vz_t
        
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
    plt.axis([0, 1.1*t, z_t, np.max(Mz[ : , 1 ])*1.1])
    plt.grid()
    plt.xlabel("temps t (en s)")
    plt.ylabel("position z(t) (en m)")
    plt.title("Equation horaire de la position z(t) d'un objet a l'instant t")
    plt.show()
    
    
    # Plot 2: [ t , x_t ]

    plt.plot( Mx[ : , 0 ] , Mx[ : , 1 ], color='g', label='num')
    plt.axis([0, 1.1*t, 0, np.max(Mx[ : , 1 ])*1.1])
    plt.grid()
    plt.xlabel("temps t (en s)")
    plt.ylabel("position x(t) (en m)")
    plt.title("Equation horaire de la position x(t) d'un objet a l'instant t")
    plt.show()
    

    # Plot 3: [ t , vz_t ]
    
    plt.plot( Mvz[ : , 0 ] , Mvz[ : , 1 ], color='b', label='num')
    plt.axis([0, 1.1*t, np.min(Mvz[ : , 1 ])*1.1, z_t])
    plt.grid()
    plt.xlabel("temps t (en s)")
    plt.ylabel("vitesse v_z(t) (en m)")
    plt.title("Equation horaire de la vitesse v_z(t) d'un objet a l'instant t")
    plt.show()
        
        
    # Plot 4: [ t , vx_t ]
    
    plt.plot( Mvx[ : , 0 ] , Mvx[ : , 1 ], color='m', label='num')
    plt.axis([0, 1.1*t, 0, np.max(Mvx[ : , 1 ])*1.1])
    plt.grid()
    plt.xlabel("temps t (en s)")
    plt.ylabel("vitesse v_x(t) (en m)")
    plt.title("Equation horaire de la vitesse v_x(t) d'un objet a l'instant t")
    plt.show()
        
        
    # Plot 5: equation de la trajectoire [ x_t , z_t ]
    
    plt.plot( M_trajectoire[ : , 0 ] , M_trajectoire[ : , 1 ], color='k', label='num')
    plt.axis([0, 1.1 * x_t , 0, 1.1 * z_0 ])
    plt.grid()
    plt.xlabel("position x(t) (en m)")
    plt.ylabel("position z(x) (en m)")
    plt.title("Equation de la trajectoire")
    plt.show()
    
    
    # Calcul de l'erreur relative E_n et de l'erreur relative logarithmique log(E(n))
        
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
                
                            
        L.append([k, abs(z_ta - (- 0.5 * g + v_0 * math.sin(alpha) + z_0))])
            
        LL.append([log10(k), log10(abs(z_ta - (- 0.5 * g + v_0 * math.sin(alpha) + z_0)))])
        
        
    M = np.array(L)    
    
    plt.plot( M[ : , 0 ] , M[ : , 1 ], color='r')
    plt.axis([-10, 110, -10, 10])
    plt.grid()
    plt.xlabel("n")
    plt.ylabel("E(n)")
    plt.title("Erreur relative")
    plt.show()
    
    
    MM = np.array(LL)
    
    plt.plot( MM[ : , 0 ] , MM[ : , 1 ], color='b')
    plt.axis([-log10(10), log10(1100), -log10(1000), log10(100)])
    plt.grid()
    plt.xlabel("log(n)")
    plt.ylabel("log(E(n))")
    plt.title("Erreur relative Log")
    plt.show()
    
    """new_array = M_trajectoire
    file = open("sample.txt", "w+")
    content = str(new_array)
    file.write(content)
    file.close()
    file = open("sample.txt", "r")
    content = file.read()
    print("Fichier sample.txt cree: SUCCES ", content)
    file.close()"""
    
    """new_array2 = Mz
    file = open("sample2.txt", "w+")
    content2 = str(new_array2)
    file.write(content2)
    file.close()
    file = open("sample2.txt", "r")
    content2 = file.read()
    print("Fichier sample2.txt cree: SUCCES ", content2)
    file.close()"""