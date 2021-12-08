import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stat

#------------------------------Mesures Plan Incliné------------------------------------------------------

K=[100,12.7,4.30,3.18,2.78,2.57,2.45,2.37,2.31,2.26,2.20,2.18] 

angle=[42,40,36,41,37,42,43,40]
masse=[831,542,344,484,325,454,593,273]

#plt.bar(angle, masse)

angle2=[37,36,36,35,38,37,38] #41,39
masse2=[460,1482,615,905,1098,992,760] #890,450

angle3=[35,39,32,33]
masse3=[660,3940,845,1367]

def trait(a,m):
    sigma1=np.std(a)
    sigma2=np.std(m)
    moy1=np.mean(a)
    moy2=np.mean(m)
    k=K[len(a)]
    incert1=k*sigma1/np.sqrt(len(a))
    incert2=k*sigma2/np.sqrt(len(a))
    print('angle=',moy1,'+-',incert1,'masse=',moy2,'+-',incert2)
    return [moy1,incert1,moy2,incert2]

dmax = trait(angle,masse)
d08 = trait(angle2,masse2)
d04 = trait(angle3,masse3)

Result=[dmax,d08,d04]

plt.bar([1300,800,400], [k[0]-30 for k in Result], width=300,bottom=30, yerr = [k[1] for k in Result])
plt.ylabel("angle de départ")

#plt.bar([1300,800,400], [k[2]-400 for k in Result], width=100, bottom=400, yerr = [k[3] for k in Result])
#plt.ylabel("masse de l'avalanche")

plt.xlabel("nb arbes par hectare")
plt.show()


#----------------------------------Collectifs Celliers---------------------------------------------------

Longueur= [23.60,24,25.5,26.10,32.1,28.40,21,27.10,30.70]
Largeur= [13.90,9.40,11.40,13.70,11.80,14,14,12.96,12.20]
arbres= [54,30,29,48,32,55,32,61,59]

bins = [k for k in range(20,38,4)]

X=np.linspace(20,38,1000)
avg=np.mean(Longueur)
sigma=np.std(Longueur)
Y=36*stat.norm.pdf(X,avg,sigma)
#plt.plot(X,Y)
#plt.hist((Longueur), bins=bins)

#plt.show()