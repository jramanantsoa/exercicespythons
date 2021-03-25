from math import pi

#Écrire un programme qui, à partir de la saisie d'un rayon et d'une hauteur, calcule le volume d'un cône droit.
rayon = float(input("Rayon :"))
hauteur = float(input("hauteur : "))
#π × R2 × h ÷ 3
print(pi*rayon*rayon*hauteur/3)