from numpy import *

from constantes import *


def produitScalaire (a, b):
    
    # Erreur
    dimension = len (a)
    if dimension != len (b):
        print ("Erreur : produit scalaire impossible entre 2 vecteurs de dimensions différentes")
        exit (0)
    
    # <a, b> = xa xb + ya yb
    resultat = 0
    for composante in range (dimension):
        resultat += a [composante] * b [composante]
    
    # Sortie
    return resultat


def intersecte (directionRayon, sphere):
    
    # Initialisation
    centre = sphere ["centre"]
    xc, yc, zc = centre
    xd, yd, zd = directionRayon
    
    # Calcul du point projeté P
    scalCD = produitScalaire (centre, directionRayon)
    coef = scalCD / produitScalaire (directionRayon, directionRayon)
    xp = xd * coef
    yp = yd * coef
    zp = zd * coef
    
    # La droite du rayon devient une demi-droite d'origine (0 ; 0 ; 0)
    if zp < origine [2]:
        xp, yp, zp = origine
    
    # Calcul des distances
    vectOP = (xp, yp, zp)
    vectCP = (xp - xc, yp - xc, zp - zc)
    distOPcarre = produitScalaire (vectOP, vectOP)
    distCPcarre = produitScalaire (vectCP, vectCP)
    
    # Retournons la distance OP ssi la sphère est visible
    if distCPcarre <= (sphere ["diametre"] / 2) ** 2:
        return (True, distOPcarre)
    else:
        return (False, None)


def couleurAffichee (directionRayon, spheres):
    
    # Initialisation
    distMin = float ('inf')
    couleur = blanc
    
    # Pour chaque sphère visible,
    for sphere in spheres:
        visible, eloignement = intersecte (directionRayon, sphere)
        if visible:
            
            # Minimisons son éloignement
            if distMin > eloignement:
                distMin = eloignement
                couleur = sphere ["couleur"]
                
    # Sortie
    return couleur


def camera (spheres, focale = 1000, largeur = 1080, longueur = 1920):
    
    # Erreur
    if focale <= 0:
        print ("Erreur : l'écran se place forcément devant la caméra")
        exit (0)
    
    # Partons d'un fond blanc
    base = [[blanc for _ in range (longueur)] for _ in range (largeur)]
    
    # Pour chaque pixel de l'écran,
    for xRayon in range (longueur):
        for yRayon in range (largeur):
            
            # La couleur du pixel devient celle de la sphère la plus proche
            directionRayon = (xRayon - longueur // 2, yRayon - largeur // 2, focale)
            base [yRayon] [xRayon] = couleurAffichee (directionRayon, spheres)
    
    # Transmettons l'image au programme de test
    return array (base)
