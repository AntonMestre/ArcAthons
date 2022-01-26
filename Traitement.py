import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
from scipy.optimize import fsolve

def traitement(dim_cible,coord_m1,coord_m2,coord_m3,data) :

    """
    Parametres : 
        dim_cible : (largeur*hauteur) en mètres
        coord_mi : (xi,yi) coordonnées du micro i
        data : [(ordre micro i, délai (en secondes absolu entre signal micro i et le premier)]
    Remarque :
        coordonnées avec un repère placé au centre de la cible"""

    tab_coord = [coord_m1,coord_m2,coord_m3]

    ordre_micro = [couple[0] for couple in data]
    

    deltaD12 = data[1][1]*340
    deltaD13 = data[2][1]*340


    tab_coord_ordre = []

    for i in ordre_micro :
        tab_coord_ordre.append(tab_coord[i-1])

    [(x1,y1),(x2,y2),(x3,y3)] = tab_coord_ordre

    largeur,hauteur = dim_cible

    mpl.rcParams['lines.color'] = 'k'
    mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color', ['k'])

    x = np.linspace(-largeur/2, largeur/2, 400) #400 points par dimensions modifiable
    y = np.linspace(-hauteur/2, hauteur/2, 400)

    x, y = np.meshgrid(x, y)

    def axes():
        plt.axhline(0, alpha=.1)
        plt.axvline(0, alpha=.1)

    def parabole1(x,y) :
        return 4*(deltaD12**2)*((x-x2)**2+(y-y2)**2) - ((x-x1)**2 + (y-y1)**2 - (x-x2)**2 - (y-y2)**2 - deltaD12**2)**2

    def parabole2(x,y) :
        return 4*(deltaD13**2)*((x-x3)**2+(y-y3)**2) - ((x-x1)**2 + (y-y1)**2 - (x-x3)**2 - (y-y3)**2 - deltaD13**2)**2


    def f(input):
        xi,yi = input
        res = np.zeros(2)
        res[0] = parabole1(xi,yi)
        res[1] = parabole2(xi,yi)
        return res


    x0 = np.array(tab_coord_ordre[0])
    solution = fsolve(f, x0)
    print(solution)
    

    axes()

    plt.contour(x, y, parabole1(x,y), [0], colors='k')
    plt.contour(x, y, parabole2(x,y), [0], colors='r')

    # img_cible = np.array(Image.open('.\Traitement\cible.png'),dtype=np.uint8)

    # fig,ax = plt.subplots(1)

    # ax.set_xlim(-largeur/2, largeur/2)
    # ax.set_ylim(-hauteur/2, hauteur/2)

    # ax.imshow(img_cible)

    # circle = patches.Circle(solution[0],solution[1])

    # #ax.add_patch(circle)

    plt.show()
    return solution

# traitement((2,2),(-1,1),(1,1),(1,-1),[(1,0),(2,0.9),(3,0.7)])