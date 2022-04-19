import math
import numpy as np
import matplotlib.pyplot as plt

def Phugoide_linearise(x_0, z_0, v_0, alpha, Cx, Cp, dt, n):
    
    #g = 10
    t = 0
    S = 0.02
    rho = 1.2
    m = 0.009
    Kz = (rho*Cp*S)/(2*m)
    f = Cp/Cx

    z_tb = z_0
    x_tb = x_0  
        
    L_zb=[]
    L_zb.append([ t , z_tb ])
    
    L_xb = []
    L_xb.append([ t , x_tb ])
    
    L_trajectoire = []
    L_trajectoire.append([x_tb, z_tb])


    while z_tb > 0:
        
        # Chronophotographie
        
        t += dt


        # PFD linéarisé
        
        print("x_tb = "+str(x_tb))
        print("z_tb = "+str(z_tb))
        
        x_tb = v_0*math.cos(alpha)*t + math.exp(- (Kz*v_0*t)/f) * (0.1*x_0*math.cos(Kz*v_0*t) + ( (0.1*v_0*math.cos(alpha))/(Kz*v_0) + (0.1*x_0)/f ) * math.sin(Kz*v_0*t) ) + x_0
        z_tb = -v_0*math.sin(alpha)*t + math.exp(- (Kz*v_0*t)/f) * (0.1*z_0*math.cos(Kz*v_0*t) + ( (0.1*v_0*math.sin(alpha))/(Kz*v_0) + (0.1*z_0)/f ) * math.sin(Kz*v_0*t) ) + z_0
        
        L_zb.append([ t , z_tb ])
        L_xb.append([t , x_tb])
        L_trajectoire.append([ x_tb , z_tb ])

    M_zb = np.array(L_zb) # matrice de [ t , z_tb ]
    
    M_xb = np.array(L_xb) # matrice de [ t , x_tb ]
    
    M_trajectoire = np.array(L_trajectoire) # matrice de [ x_tb , z_tb ]
            
    
    # plot creation (graph)
    
    # plot ( t , z(t) )

    plt.plot( M_zb[ : , 0 ] , M_zb[ : , 1 ], color='g', label='pfd')
    plt.axis([0, 1.1*t, z_tb, np.max(M_zb[ : , 1 ])*1.1])
    plt.grid()
    #plt.axis([0,4,0,5])
    plt.xlabel("temps t (en s)")
    plt.ylabel("position z(t) (en m)")
    plt.title("Equation horaire de la position z(t) d'un objet à l'instant t")
    plt.show()
    
    # plot ( t , x(t) )

    plt.plot( M_xb[ : , 0 ] , M_xb[ : , 1 ], label='pfd')
    plt.axis([0, 1.1*t, -1, np.max(M_xb[ : , 1 ])*1.1])
    plt.grid()
    plt.xlabel("temps t (en s)")
    plt.ylabel("position x(t) (en m)")
    plt.title("Equation horaire de la position x(t) d'un objet à l'instant t")
    plt.show()
    
    # plot ( x(t) , z(t) )

    plt.plot( M_trajectoire[ : , 0 ] , M_trajectoire[ : , 1 ], label='pfd')
    plt.axis([0, np.max(M_xb[ : , 1 ])*1.1, 0, 1.1 * z_0 ])
    plt.grid()
    plt.xlabel("position x(t) (en m)")
    plt.ylabel("position z(t) (en m)")
    plt.title("Equation de la trajectoire")
    plt.show()