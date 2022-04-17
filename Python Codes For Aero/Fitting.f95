program Coef_calc
implicit none

integer                             :: i,j,k,l,m,n,PreCz,nbrrow
real                                :: Vnorme,dt,Cx,Cz,alpha,mg,rhoS,eps,S,val1,val2
real, DIMENSION(:),ALLOCATABLE      :: Xn,Zn
REAL, DIMENSION(:),ALLOCATABLE      :: Vnx,Vnz,Anx,Anz
REAL, DIMENSION(:),ALLOCATABLE      :: T
Real, Dimension(:,:),allocatable    :: Comp
Real, Dimension(4)                  :: vali=(/0.,0.,0.,0./)

n = 100

!set up des tableaux avec une taille n
allocate(Xn(n),Zn(n),Vnx(n),Vnz(n),Anx(n),Anz(n),T(n))

!nombre de valeurs pour les cx et cz
PreCz = 100

Anx(0)= 0
Anz(0)= -10
Vnx(0) = 0
Vnz(0) = 0
! Penser à changer les valeur de Z0 et X0 en fonction du fichier utilisé
Xn(0) = 0
Zn(0) = 0
T(0)= 0
dt = 0.04

i=0
eps = 100000

!L'idée de l'agorithme est de calculer les trajectoires pour un grand nombre de Cx,Cz, vx0, vz0 et de prendre celle qui correspond le plus aux données expérimentales

nbrrow=0
open(1, file = 'coef_calc4.dat',form='formatted', status = 'old')
do i= 1,100
  ! lecture des deux colonnes
  read(1,*, end=99) val1, val2
 nbrrow = nbrrow+1
 
enddo 
99 Close(1)
Print*, "nbrrow =",nbrrow

AlLoCaTe(Comp(nbrrow,2))

open(1, file = 'coef_calc4.dat',form='formatted', status = 'old')
do i= 1,nbrrow
  ! lecture des deux colonnes
  read(1,*, end=999) val1, val2
  Comp(i,:) = (/val1,val2/)
enddo 
999 Close(1)

Do i = 1,nbrrow
	Print*, Comp(i,1),"	", Comp(i,2)
enddo

Xn(0) = Comp(1,1)
Zn(0) = Comp(1,2)

! boucle l pour les vitesses selon x
do l = 0,20
	Vnx(0) = l*0.01
	Print*, Vnx(0)
	! boucle m pour les vitesses selon z
	do m = -150,-100
		Vnz(0) = m*0.01
		Do j= 30,PreCz
			Cz = j*0.01
			do k = 10,j/2
				Cx = k*0.01
				S = 0
				i=0
				do while  (nbrrow > i-1)
	
					i=i+1
		
					! Calcul du temps
					T(i)= T(i-1)+dt
	
					! Méthode des différences finies explicite
					! -1/2*rho*S*C*V² équivalent à const * V²
					Vnorme = ((Vnx(i-1)**2)+(Vnz(i-1))**2)**0.5
	
					Anx(i) = Anx(0) - (Vnorme)*(Cx*Vnx(i-1) + Cz*Vnz(i-1))
					Anz(i) = Anz(0) - (Vnorme)*(Cx*Vnz(i-1) - Cz*Vnx(i-1))
	
					Vnx(i) = Vnx(i-1) + Anx(i)*dt
					Vnz(i) = Vnz(i-1) + Anz(i)*dt
	
					Xn(i) = Xn(i-1) + Vnx(i)*dt
					Zn(i) = Zn(i-1) + Vnz(i)*dt
					
					! Calcul des erreurs tous les 5,8,9,11 points du graph afin d'évaluer une courbe lissée des résultats expérimentaux
					if (modulo(i+8,9) == 0) then
						S = S + (((Comp(i,2)-Zn(i))**2 +  (Comp(i,1)-Xn(i))**2)  **0.5)
					endif
				enddo
				! Comparaison en fonction de la norme de l'erreur : racine de (errX²+errZ²)
				if (eps > S) then
					eps = S
					!Print*, "S=",S
					vali = (/Cx,Cz,Vnx(0),Vnz(0)/)
					!Print*, "ok étape", "Cx =", vali(1), "  Cz =", vali(2), "  Vx0 =", vali(3), " Vz0 =", vali(4)
					!print*," "
				endif
			enddo
		enddo
	enddo
enddo

Print*, "Cx =", vali(1), "  Cz =", vali(2),  "  Vx0 =", vali(3), " Vz0 =", vali(4), "Xn(0)= ", Xn(0),"Zn(0)= ", Zn(0),"S =", S
Close(1)

end program Coef_calc







