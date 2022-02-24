import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Dates interressantes : 
#[63575:63718],[78691:78834],[63237:63380]
#[28608:28674],[43724:43790],[28607:28673]

temp_air = pd.read_table("/Users/cyrian/Desktop/SpéBio1/TIPE/Info TIPE/Données météo/Morin_2012/datasets/Data_CDP_met_insitu.tab")
temp_air = pd.DataFrame(temp_air)
temp_surfneige = pd.DataFrame(pd.read_table("/Users/cyrian/Desktop/SpéBio1/TIPE/Info TIPE/Données météo/Morin_2012/datasets/Data_CDP_hor_eval.tab"))
temp_disk = pd.DataFrame(pd.read_table("/Users/cyrian/Desktop/SpéBio1/TIPE/Info TIPE/Données météo/Morin_2012/datasets/Data_CDP_hor_disk.tab"))
Date = temp_air["Date/Time"]
Date = pd.to_datetime(Date)
Date = list(Date[63575:63718])
Tair = temp_air["TTT [°C]"]
Tair = Tair[63575:63718]
Tsurf = temp_surfneige["t [°C] (at snow surface, upward IR ra...)"]
Tsurf = Tsurf[78691:78834]
Tdisk1 = temp_disk['t [°C] (attached to settling disk 8, ...)']
Tdisk1 = Tdisk1[63237:63380]
Tdisk2 = temp_disk['t [°C] (attached to settling disk 9, ...)']
Tdisk2 = Tdisk2[63237:63380]
Tdisk3 = temp_disk['t [°C] (attached to settling disk 11,...)']
Tdisk3 = Tdisk3[63237:63380]

#print (temp_air)
#print(Date[0],Date[99])
#print(Tair)
#print(Tsurf

plt.plot(Date,Tair,'red')
plt.plot(Date,Tsurf,'blue')
plt.plot(Date,Tdisk1,'green')
plt.plot(Date,Tdisk2,'green')
plt.plot(Date,Tdisk3,'green')
plt.show()