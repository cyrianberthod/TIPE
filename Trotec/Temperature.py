import pandas as pd
import matplotlib.pyplot as plt
#[3880:6398]
#[640:3697]

DataC = pd.read_table("/Users/cyrian/Desktop/SpéBio1/TIPE/Info TIPE/Trotec/Clairière.tab")
TC = DataC['   Temp              ']
TC=TC[3880:6398]
HumidC = DataC['  %RH              ']
HumidC = HumidC[3880:6398]
DateC = DataC[' Heure ']
DateC=DateC[3880:6398]
DateC = pd.to_datetime(DateC)

DataF = pd.read_table("/Users/cyrian/Desktop/SpéBio1/TIPE/Info TIPE/Trotec/Forêt.tab")
TF = DataF['   Temp              ']
TF=TF[3880:6398]
HumidF = DataF['  %RH              ']
HumidF = HumidF[3880:6398]
DateF = DataF[' Heure ']
DateF=DateF[3880:6398]
DateF = pd.to_datetime(DateF)


#plt.scatter(DateC,TC,color='grey')
#plt.scatter(DateC,TF,color=(0,0.6,0))
print('Amp foret =',max(TF)-min(TF))
print('Amp clairière =',max(TC)-min(TC))

plt.scatter(DateC,HumidC,color='grey', marker='.')
plt.scatter(DateC,HumidF,color=(0,0.6,0),marker='.')

plt.xlabel("Temps (Mois-Jour Heure)")
#plt.ylabel("Température (°C)")
plt.ylabel("Humidité (%)")
handles = [plt.Rectangle((0,0),1,1,color=c,ec="k")for c in ['grey',(0,0.4,0)]]
labels= ["Clairière", "forêt"]
plt.legend(handles,labels)

plt.show()