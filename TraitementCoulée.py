##importations
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as img
import matplotlib.patches as patches
import ee
#ee.Authenticate()
ee.Initialize()
import math 
#global lat1,lon1,lat2,lon2,lx,ly,largeur,hauteur

#--------------Récupération de la carte CLPA------------------------------------------------------------------------------------

#ouverture d'une carte
imgfile=""#lien du chemin d'accès à la carte 
matriceCLPA=np.array(Image.open(imgfile).convert('RGB')) #convertion de la carte en matrice
ly,lx,bin=matriceCLPA.shape #renvoie la taille de l'image en pixel


#recupération des coordonées GPS


lat1=45.95795554778 #float(input('lat coin haut gauche=')) #QGIS 
lon1=6.48127237609 #float(input('lon coin haut gauche='))
lat2=45.88692231036#float(input('lat coin bas droit='))
lon2=6.61231466549 #float(input('lon coin bas droit='))
largeur=lon2-lon1
hauteur=lat1-lat2


#convertion des coord de pixel en coord GPS
def coordGPS(x,y): 
    lat=lat1-y*(hauteur/ly)
    lon=lon1+x*(largeur/lx)
    return (lat,lon)

#-----------------Sélection d'un polygone contenant la coulée sur la CLPA---------------------------------------------------------------------------------

while True: #tant qu'on ne fait rien la carte reste affichée 
    data = [] #coord en pixel des points du polygone
    while len(data) < 3:
        image = img.imread(imgfile) #ouverture carte CLPA
        fig, ax=plt.subplots(frameon=False)
        fig.set_size_inches(lx/767,ly/767) #met la figure à la même taille que la CLPA
        ax.imshow(image,cmap="gray") # affichage image CLPA
        data = np.asarray(plt.ginput(-1, timeout=-1)) #entre matrice dans data, plt.ginput = tracer pts, "-1" = on peut faire autant de pts qu'on veut, appuie sur entrée arrête ginput
       
    # Le polygone apparait bleu
    counter = plt.fill(data[:, 0], data[:, 1], facecolor=(0,0,1), edgecolor='#000000', linewidth= 0.1) #forme polygone dont 4pts sont les angles et le remplis en bleu (plus tard prendra que ce qui est rouge en dessous de ce qui est bleu)
    plt.axis('off')
   # plt.figure(figsize=(ly/1000, lx/1000), dpi=96) #met a l'echelle la figure
    plt.draw()#affichage polygone
    plt.savefig('polygone.jpg',dpi=1000,bbox_inches='tight',pad_inches=0)#sauvegarde figure tracée sur une image, dpi = nb pixel par pouce, bbox et pad sauv sans bordures
    
    #sortie de la carte en appuyant sur une touche de clavier
    if plt.waitforbuttonpress():
        break   

polygone=Image.open('polygone.jpg')
#polygone.show() 


#-----------------Sélection de la coulée dans le polygone, obtention de la liste des coordonées GPS des points de la coulée---------------------------------------------------------------------------------

#def des couleurs sélectionnées
ri,gi,bi=180,50,50 #borne inf
rs,gs,bs=255,100,100 #borne sup

precoulée=[]
 
matricePoly=np.array(polygone)#figure=>image=>matrice
print(matricePoly.shape)#à RETIRER
print(matriceCLPA.shape)
CLPAcopie=matriceCLPA.copy() #pour pv la modifier

for x in range(lx):
    for y in range(ly):
        color=matricePoly[y,x,] #couleurs des pts de l'image avec poly
        r,g,b = color[0],color[1],color[2]
        if r<10 and g<10 and b>245:
            color=matriceCLPA[y,x,] #extraire la couleur
            r,g,b=color[0],color[1],color[2]
            if ri<r<rs and gi<g<gs and bi<b<bs:
                 CLPAcopie[y,x,]=[255,0,0]
                 precoulée.append(coordGPS(x,y)) #si bleu dans matricePoly et rouge dans matriceCLPA alors =coulée
            else:
                 CLPAcopie[y,x,]=[255,255,255] #sinon pts devient blanc
       
        else:
            CLPAcopie[y,x,]=[255,255,255] #sinon pts devient blanc

#Vérification coulée sélectionnée et séparée des autres
image=Image.fromarray(CLPAcopie) #CLPAcopie tous pts sélectionnés = rouges, les autres = blancs
image.show()

#on prend un point sur 10 pour former la liste coulée
coulée=[]
for k in range (0,len(precoulée),20):
    coulée.append(precoulée[k])

print(coulée)
print(len(coulée))


#-----------------Traitement de la liste 'coulée' obtenue---------------------------------------------------------------------------------


#données ee d'altitude:

def zpt(x,y): #renvoie l'altitude pour un pt de coordonnées (x,y)    
    alt=ee.Image('USGS/SRTMGL1_003')
    u=ee.Geometry.Point(y,x) #longitude,latitude dans l'ordre
    scale=1 #en mètre
    z=alt.sample(u,scale).first().get('elevation').getInfo()
    return z 


def recupente(coulée): #renvoie la pente, le dénivelé, la longueur, l'altitude min et l'altitude max
    Lalt=[] #liste des altitudes de chaque point
    for coord in coulée: #trouve zmin et z max
        x,y= coord
        Lalt.append(zpt(x,y))
    Laltcopy=sorted(Lalt) #trie la liste des alt
    zmax,zmin=max(Lalt),min(Lalt) #l'altitude min et l'altitude max
    deltaz=zmax-zmin #le dénivelé

    i,j=Lalt.index(zmax),Lalt.index(zmin) #indices du pt de zmax et du point de zmin
    
    #récupération des coordonnées géographiques
    (xmax,ymax)=coulée[i] #x=lat , y=lon
    (xmin,ymin)=coulée[j]
  
    
    deltay=(ymax-ymin)*40000000*math.cos(math.radians(xmin))/360
    deltax=111111*(xmax-xmin)
    d=(deltay**2+deltax**2)**0.5  #longueur de la coulée (calcule avec Pythagore)
    
    pente=math.degrees(math.atan((zmax-zmin)/d)) #calcule la pente
  
    return (pente,deltaz,d,zmin,zmax) #différence d'altitude 

def analyse(coulée): #renvoie la densité d'arbres par tronçon d'une coulée + dtot + pente
    fnf=ee.ImageCollection("JAXA/ALOS/PALSAR/YEARLY/FNF")
    a1,a2,a3= 0,0,0 #nb arbres par tronçon
    n1,n2,n3=0,0,0 #nb total de pts par tronçon
    pente,deltaz,distance,zmin,zmax=recupente(coulée) 
    div=deltaz/3 #divise la coulée en 3 tronçons
    for coord in coulée:
        x,y=coord
        point = ee.Geometry.Point(y,x) #longitude,latitude
        arbreannée=fnf.getRegion(point,1).getInfo() # arbre liste de listes d'info par années
        if zpt(x,y)<=div+zmin: #1er tronçon
            n1+=1
            if arbreannée[1][-1]==1: #arbre[1][-1] on recuperer le dernier terme (info présence arbre) 1ere année
                a1+=1
        elif div+zmin<zpt(x,y)<2*div+zmin: #2ème tronçon
            n2+=1
            if arbreannée[1][-1]==1:
                a2+=1
        else:               #3ème tronçon
            n3+=1
            if arbreannée[1][-1]==1:
                a3+=1
                
    dataCoulée=[a1/n1,a2/n2,a3/n3,(a1+a2+a3)/(n1+n2+n3),pente,pente1tiers,deltaz,distance,zmin,zmax]#(darbre1ertronçon, darbre2emetronçon, darbre3emetronçons,d totale, pente, dénivelé, longueur coulée, alt min, alt max)


    return dataCoulée 
