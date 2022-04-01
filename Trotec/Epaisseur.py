import matplotlib.pyplot as plt
import numpy as np


F1=[90,55,65,90,120,130,85,100,85,140]
C1=[120,115,120,120,120,115,115,110,110,110]

F2=[100,80,85,105,130,155,145,115,110,145]
C2=[135,135,135,135,130,130,130,130,135,135]

F=[]
C=[]

for k in range(10):
    F.append(F2[k]-F1[k])
    C.append(C2[k]-C1[k])
    

print(np.std(C),np.std(F))

def interv(L):
    K=[100,12.7,4.30,3.18,2.78,2.57,2.45,2.37,2.31,2.26,2.20,2.18] 
    sigma=np.std(L)
    k=K[len(L)]
    incert=k*sigma/np.sqrt(len(L))
    return incert

plt.bar([0,1.5], [np.average(C),np.average(F)], width=1, bottom=0, yerr=[interv(C), interv(F)], color=['grey',(0,0.4,0)])
#plt.hist((C1,F1), bins=[k for k in range(50,160,25)], color=['grey',(0,0.4,0)])
plt.xticks(color="None")
plt.ylabel("Epaisseur de la couche de neige nouvellement formée (cm)")

#plt.scatter([k for k in range (0,10)], C1, c="grey")
#plt.scatter([k for k in range (0,10)], F1, c=(0,0.4,0))
#plt.scatter([k for k in range (0,10)], C2, c="grey")
#plt.scatter([k for k in range (0,10)], F2, c=(0,0.4,0))


#plt.plot([k for k in range (0,10)], C1, c="grey")
#plt.plot([k for k in range (0,10)], F1, c=(0,0.4,0))
#plt.plot([k for k in range (0,10)], C2, c="grey")
#plt.plot([k for k in range (0,10)], F2, c=(0,0.4,0))

#plt.xlabel("Déplacement latéral(m)")
#plt.ylabel("Epaisseur du manteau neigeux (cm)")
handles = [plt.Rectangle((0,0),1,1,color=c,ec="k")for c in ['grey',(0,0.4,0)]]
labels= ["clairière", "forêt"]
plt.legend(handles,labels)





plt.show()