import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#longueur coulée = f(d arbre , pente)
#nb coulée = f(d arbre , pente)
#d arbre = f(pente , alt max)

Data=[[1.0, 0.07650273224043716, 0.0, 0.21608040201005024, 29.11887775559068, 38.08291850418205, 662, 1188.457622528473, 1196, 1858], [1.0, 0.5625, 0.0, 0.4444444444444444, 31.207670224424803, 31.470817296759943, 316, 521.6204123498161, 1232, 1548], [1.0, 0.8431372549019608, 0.0, 0.5272727272727272, 32.079593255301745, 38.51302008188361, 799, 1274.7234707749706, 1108, 1907], [1.0, 0.6151685393258427, 0.7533875338753387, 0.7327080890973037, 24.283025105614527, 31.15286859882105, 427, 946.4476984724582, 1438, 1865], [0.007142857142857143, 0.0, 0.0, 0.0045871559633027525, 25.088479741161127, 36.780794881557455, 308, 657.8538933872748, 1824, 2132], [0.036585365853658534, 0.0, 0.0, 0.012, 23.54104098603282, 21.102457049228114, 310, 711.5569330737654, 1618, 1928], [0.0, 0.0, 0.0, 0.0, 30.565843916888422, 25.851846406333625, 206, 348.80137685032224, 1729, 1935], [0.0, 0.0, 0.0, 0.0, 36.36650517244682, 31.579719255900066, 246, 334.074989958095, 1739, 1985], [0.0, 0.0, 0.0, 0.0, 26.60604059315036, 41.94959291850707, 569, 1135.9675938559635, 1730, 2299], [0.0, 0.0, 0.0, 0.0, 39.43297772859761, 49.25837033738022, 340, 413.4373806768667, 1752, 2092], [0.0, 0.0, 0.0, 0.0, 33.53749545571398, 28.23359992999491, 197, 297.21175345360007, 1619, 1816], [0.0, 0.0, 0.15151515151515152, 0.08450704225352113, 25.806663235342718, 25.897374672163597, 386, 798.2424289270773, 1866, 2252], [0.0, 0.0, 0.0, 0.0, 26.433670120972575, 40.00335862554407, 711, 1430.1892997795348, 2699, 3410], [0.0, 0.0, 0.0, 0.0, 25.654691175350592, 24.234050960350825, 435, 905.6954121310987, 2802, 3237], [0.5384615384615384, 0.01606425702811245, 0.0, 0.04641775983854692, 26.833374526888345, 26.39578793240221, 1253, 2476.9322594243704, 1444, 2697], [0.2, 0.0, 0.0, 0.002066115702479339, 27.21519891637165, 28.310083468014632, 1341, 2607.6021235607905, 1730, 3071], [0.725, 0.028368794326241134, 0.0, 0.047042052744119746, 28.18692003889227, 32.55531169974958, 1528, 2851.2707274715412, 1453, 2981], [0.22809457579972184, 0.30656934306569344, 0.0, 0.18674698795180722, 25.03264073081631, 25.811485168167252, 927, 1985.0047330593095, 1470, 2397], [0.0, 0.0, 0.0, 0.0, 24.902669210668346, 17.408478498482545, 310, 667.7563719161053, 2109, 2419], [0.24154589371980675, 0.015345268542199489, 0.0, 0.06015037593984962, 26.520069038665167, 27.006522006831172, 1193, 2390.6904062067474, 1454, 2647], [0.0, 0.0, 0.0, 0.0, 25.307065343306764, 28.783177465023776, 886, 1873.7494269730248, 2307, 3193], [0.0, 0.0, 0.0, 0.0, 27.746537021478307, 46.174840111659165, 734, 1395.3091825523472, 2453, 3187], [0.10869565217391304, 0.07894736842105263, 0.0, 0.05701754385964912, 35.4192001307535, 40.95522288666176, 448, 629.9500669860529, 1698, 2146], [0.453125, 0.0, 0.0, 0.17261904761904762, 30.025565439292365, 32.197478929696786, 719, 1244.062247224729, 2178, 2897], [0.9333333333333333, 0.0, 0.0, 0.15155615696887687, 28.65200202059337, 32.423260233914036, 873, 1597.7432140874523, 2008, 2881], [1.0, 1.0, 0.7718120805369127, 0.8645418326693227, 25.935401980684162, 30.815857940595368, 773, 1589.4305343364192, 1687, 2460], [0.9607843137254902, 0.010416666666666666, 0.0, 0.096045197740113, 23.455973344864038, 23.486939716485903, 557, 1283.708902659274, 2024, 2581], [0.0, 0.0, 0.0, 0.0, 28.881828379039657, 36.539518344312604, 916, 1660.5756927323089, 2318, 3234], [0.9878542510121457, 0.12545454545454546, 0.0, 0.3351177730192719, 31.33664393887861, 36.74514646096158, 1102, 1809.8630259492893, 1747, 2849], [1.0, 0.17905405405405406, 0.0, 0.26727509778357234, 31.672658343395916, 36.68052029941769, 1273, 2063.3644014416764, 1692, 2965], [0.6674364896073903, 0.006472491909385114, 0.0, 0.2623985572587917, 32.83540253031886, 30.545460713953524, 1349, 2090.4004872831874, 1929, 3278], [0.9632352941176471, 0.0, 0.0, 0.1585956416464891, 28.75152040699126, 30.105118259152423, 1518, 2766.7745221541177, 1759, 3277], [1.0, 1.0, 1.0, 1.0, 27.327319557645712, 0, 298, 576.6895773893963, 1407, 1705], [1.0, 1.0, 1.0, 1.0, 25.8152051065823, 0, 227, 469.254209201097, 1526, 1753], [1.0, 1.0, 0.8914728682170543, 0.9828850855745721, 26.611432920489268, 0, 386, 770.4401627985894, 1619, 2005], [0.8007736943907157, 0.021897810218978103, 0.0, 0.2484186313973548, 24.441913671183837, 0, 512, 1126.5065271875685, 1648, 2160], [1.0, 0.3333333333333333, 0.004975124378109453, 0.34054054054054056, 36.982329845182726, 0, 445, 590.9140244013871, 1497, 1942], [1.0, 1.0, 1.0, 1.0, 24.19515966363186, 23.216022359178435, 511, 1137.2835169805332, 1129, 1640], [1.0, 0.6368159203980099, 0.39444444444444443, 0.6367265469061876, 21.422266393762616, 25.24032071241702, 477, 1215.769554916826, 1443, 1920], [1.0, 0.8695652173913043, 0.02054794520547945, 0.1797752808988764, 29.02402458194629, 34.93961698108566, 567, 1021.8843233189739, 1256, 1823], [0.7887323943661971, 1.0, 1.0, 0.9044585987261147, 32.2758942875134, 39.38607057832354, 509, 805.9088788803509, 1176, 1685], [1.0, 1.0, 1.0, 1.0, 31.58125447477177, 33.751182654667495, 489, 795.441165179226, 1181, 1670], [0.8378378378378378, 1.0, 1.0, 0.9285714285714286, 32.11798207008815, 40.58206146275069, 579, 922.3619001361305, 1184, 1763], [0.03773584905660377, 0.19736842105263158, 0.0, 0.09444444444444444, 26.815395055402444, 37.87214818399684, 372, 735.9434080799755, 1182, 1554], [1.0, 0.6, 0.5955056179775281, 0.6770186335403726, 23.608989709881502, 22.99874811401482, 520, 1189.724119647595, 1234, 1754], [0.9375, 1.0, 1.0, 0.9761904761904762, 31.689203396158852, 33.07013665253593, 537, 869.8436804354059, 1195, 1732], [0.9259259259259259, 1.0, 1.0, 0.9577464788732394, 33.856944835497984, 41.560797513471556, 369, 550.0222979037253, 1214, 1583], [0.0, 0.024734982332155476, 0.0, 0.009446693657219974, 30.165641777613367, 32.736983289457065, 955, 1643.1199157978149, 1703, 2658], [0.343804537521815, 0.0, 0.0, 0.11257142857142857, 25.454477071857315, 28.175551344533154, 1550, 3256.2982929862283, 1698, 3248], [0.0, 0.0, 0.0, 0.0, 33.900402126135205, 43.47672061581084, 1258, 1872.0731170432598, 2326, 3584], [0.0, 0.0, 0.0, 0.0, 26.2369858448712, 28.79360106450345, 1027, 2083.7430181628797, 2223, 3250], [0.0, 0.0, 0.0, 0.0, 32.33081071461093, 33.40519174793148, 485, 766.2815031170927, 2286, 2771], [0.0, 0.0, 0.0, 0.0, 26.715002574086558, 14.421673347561565, 618, 1227.9551110328453, 2416, 3034], [0.0, 0.0, 0.0, 0.0, 29.032115648205416, 38.85750688412876, 515, 927.8576635453549, 2896, 3411], [0.0, 0.0, 0.0, 0.0, 30.080833038001785, 32.62146130611792, 1489, 2570.6413890276917, 1629, 3118], [0.0, 0.0, 0.0, 0.0, 28.935559470644733, 24.461759057058057, 580, 1049.1287190645874, 2269, 2849], [1.0, 1.0, 0.8125, 0.9338235294117647, 18.533719253960488, 15.393321512040608, 284, 847.1293954316025, 1790, 2074], [1.0, 0.6031746031746031, 1.0, 0.8922413793103449, 26.631935585370233, 28.869875059737826, 455, 907.3504563025957, 1575, 2030], [0.0, 0.0, 0.0, 0.0, 31.406134236065984, 37.62657995525258, 319, 522.4800995364327, 2633, 2952], [0.0, 0.0, 0.0, 0.0, 32.97971634076483, 27.021589531306937, 356, 548.6170289486705, 1712, 2068], [0.0, 0.0, 0.0, 0.0, 27.274810784760458, 33.73856708483356, 760, 1474.0627196039925, 2707, 3467], [1.0, 1.0, 1.0, 1.0, 30.862870399019446, 30.38281935556207, 392, 655.9485528472012, 1432, 1824], [1.0, 1.0, 1.0, 1.0, 30.34103173306091, 23.483018097405726, 339, 579.1764055676572, 1551, 1890], [1.0, 1.0, 1.0, 1.0, 27.473320928720884, 35.064604809956855, 371, 713.4953291532424, 1369, 1740], [1.0, 1.0, 1.0, 1.0, 29.90426351785165, 28.177590777933926, 295, 512.9323947675082, 1331, 1626], [1.0, 1.0, 1.0, 1.0, 35.15977703056434, 51.92795850944911, 313, 444.3677446110143, 1424, 1737], [0.08139534883720931, 1.0, 1.0, 0.38996138996138996, 26.646718202296093, 36.14264976729825, 367, 731.391900376117, 1508, 1875], [0.875, 1.0, 1.0, 0.9230769230769231, 27.276347768283056, 44.30688263009215, 215, 416.9771226090822, 1508, 1723]]
print('nb coulées =',len(Data))
Fb=[e[0]for e in Data]
Fm=[e[1]for e in Data]
Fh=[e[2]for e in Data]
F=[e[3]for e in Data]
Pente=[e[4]for e in Data]
Penteh=[e[5]for e in Data]
Deniv=[e[6]for e in Data]
Longueur=[e[7]for e in Data]
Altmin=[e[8]for e in Data]
Altmax=[e[9]for e in Data]
Altmoy=[(e[9]+e[8])/2 for e in Data]

def Graph3D(X,Y,Z): 
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    fig.add_axes(ax) 
    ax.scatter(X, Y, Z)
    ax.set_xlabel('X1', fontsize = 11)
    ax.set_ylabel('X2', fontsize = 11)
    ax.set_zlabel('y', fontsize = 11)
    plt.show()


#Graph3D(Pente,Altmoy,F)
#Graph3D(Fh,Altmax,Pente)

def Graph(X,Y): 
    plt.scatter(X, Y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

#Graph(Altmoy,F)
#Graph(Altmin,F)
#Graph(F,Longueur)
Graph(Fh,Pente)

#-------------cacractéristiques physiques des coulées--------------------------------------------------------------------------------------------

def pente():
    plt.hist((Pente), bins=[k for k in range(15,50,3)], edgecolor='black')
    plt.xlabel('pente')
    plt.ylabel('nb de coulées')
    #handles = [plt.Rectangle((0,0),1,1,color=c,ec="k")for c in ['blue','orange']]
    #labels= ["pente moy","pente de départ"]
    plt.axvline(np.average(Pente), color='blue')
    #plt.legend(handles,labels)
    plt.show()

#pente()

def alt():
    plt.hist((Altmax,Altmoy,Altmin), bins=[k for k in range(1000,4000,250)], edgecolor='black')
    plt.xlabel('Altitude')
    plt.ylabel('nb de coulées')
    handles = [plt.Rectangle((0,0),1,1,color=c,ec="k")for c in ['blue','orange','green']]
    labels= ["Altitude de départ","alt moy","Altiude d'arrivée"]
    plt.axvline(np.average(Altmoy), color='red')
    plt.legend(handles,labels)
    plt.show()

#alt()

def longueur():
    plt.hist(Longueur, bins=[k for k in range(0,4000,250)], edgecolor='black')
    plt.xlabel('Longueur')
    plt.ylabel('nb de coulées')
    plt.show()

#longueur()

def foret():
    plt.hist((F), bins=[k/100 for k in range(0,110,10)], edgecolor='black')
    plt.xlabel('proportion de foret')
    plt.ylabel('nb de coulées')
    plt.axvline(np.average(F), color='blue')
    plt.show()

#foret()

# --------------------------------------------------------------------------------------------------------

def compatroncon():
    f1=[e[2]*100 for e in Data]
    f2=[e[1]*100 for e in Data]
    f3=[e[0]*100 for e in Data]
    plt.hist((f1,f2,f3), bins=[k for k in range(0,120,20)], edgecolor='black',) #density=True)
    handles = [plt.Rectangle((0,0),1,1,color=c,ec="k")for c in ['blue','orange','green']]
    labels= ["troncon haut","troncon moyen","troncon bas"]
    plt.axvline(x=np.average(f1), color='blue', label='moy troncon haut')
    plt.axvline(x=np.average(f2), color='orange', label='moy troncon moy')
    plt.axvline(x=np.average(f3), color='green', label='moy troncon bas')
    plt.xlabel("proportion de forêt", fontsize=16)  
    plt.ylabel("nb de coulées", fontsize=16)
    plt.legend(handles, labels)

    plt.show()

#compatroncon()

def compatronconalt(altmin,altmax): #comparaison a alt fixée entre altmin et altmax
    F1,F2,F3 = [],[],[]
    for k in range (len(Data)):
        if altmin<Altmax[k]<altmax:
            F1.append(Fh[k]*100)
        elif altmin<Altmin[k]<altmax:
            F3.append(Fb[k]*100)
    #print(F1,F3)
    plt.hist((F1,F3), bins=[k for k in range(0,110,10)], edgecolor='black',) #density=True)
    handles = [plt.Rectangle((0,0),1,1,color=c,ec="k")for c in ['blue','orange']]
    labels= ["troncon haut","troncon bas"]
    plt.axvline(x=np.average(F1), color='blue', label='moy troncon haut')
    plt.axvline(x=np.average(F3), color='orange', label='moy troncon moy')
    plt.xlabel("proportion de forêt à altitude fixée à 1700m", fontsize=16)  
    plt.ylabel("nb de coulées", fontsize=16)
    plt.legend(handles, labels)

    plt.show()

#compatronconalt(1800,2000)

def compapente(altmin,altmax): #pente en fonction de prop de foret a alt fixée 
    f,p = [],[]
    for k in range (len(Data)):
        if altmin<Altmoy[k]<altmax:
            f.append(Fh[k]*100)
            p.append(Pente[k])
    Graph(f,p)

#compapente(1500,1750)
#compapente(1750,2000)

