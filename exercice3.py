#Une autre boucle while : calculez la somme d'une suite de nombres positifs ou nuls. Comptez combien il y avait de données et combien étaient supérieures à 100.
#Entrer un nombre inférieur ou égal à 0 indique la fin de la suite.

#somme
#nb_donnees
#superieur_a_cent
liste=[]
while True:
    n=input("Entrer un nombre positif ou null. Négatif pour arrêter.")
    if int(n)>=0:
        liste.append(int(n))
    else:
        print("La somme est : "+str(sum(liste)))
        print(f"Il y a {len(liste)} éléments.")
        superieur_a_cent = [x for x in liste if x > 100]
        print(f"Il y a {len(superieur_a_cent)} élément(s) supérieurs à 100")