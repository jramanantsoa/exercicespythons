#Un gardien de phare va aux toilettes cinq fois par jour. Or les WC sont au rez-de-chaussée…

#Écrire une procédure (donc sans return) hauteurParcourue qui reçoit deux paramètres, le nombre de marches du phare et la hauteur de chaque marche (en cm), et qui affiche :

#Sélectionnez
#Pour x marches de y cm, il parcourt z.zz m par semaine.
#On n'oubliera pas :

#qu'une semaine comporte 7 jours ;
#qu'une fois en bas, le gardien doit remonter ;
#que le résultat est à exprimer en m.

def hauteurParcourue(nb_de_marches,hauteur_marche_cm):
    nb_de_metres = nb_de_marches * hauteur_marche_cm * 0.001 * 2 * 7

    print(f"Pour {nb_de_marches} marches de {hauteur_marche_cm} cm, il parcourt {nb_de_metres} m par semaine.")

nb = input("nb de marches ? ")
h = input("hauteur d'une marche ? ")
hauteurParcourue(nb,h)