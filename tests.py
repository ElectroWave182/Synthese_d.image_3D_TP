import cv2
from pathlib import Path
from matplotlib import pyplot

from intersection import *


def main ():
    
    
    # Initialization
    
    nbLignes = 1
    nbColonnes = 1
    compteur = 1


    # Read images

    cheminImages = str (Path (__file__). resolve (). parent) + "/images/"
    
    
    # Treat them
    
    spheres = list ()
    spheres. append ({"centre": (0, 0, 1000), "couleur": rouge, "diametre": 767})
    spheres. append ({"centre": (0, 0, -800), "couleur": bleuEcoPlus, "diametre": 767})
    spheres. append ({"centre": (100, 150, 1200), "couleur": jaune, "diametre": 1500})
    image = camera (spheres, largeur = 1280)
    
    
    # Show result
    
    pyplot. subplot (nbLignes, nbColonnes, compteur)
    pyplot. imshow (image)
    pyplot. title ("")
    compteur += 1
    
    
    pyplot.show ()


main ()