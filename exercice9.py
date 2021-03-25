#Un permis de chasse à points remplace désormais le permis de chasse traditionnel. Chaque chasseur possède au départ un capital de 100 points. S'il tue une poule, il perd 1 point, 3 points pour un chien, 5 points pour une vache et 10 points pour un ami. Le permis coûte 200 euros.

#Écrire une fonction amende qui reçoit le nombre de victimes du chasseur et qui renvoie la somme due.

#Utilisez cette fonction dans un programme principal qui saisit le nombre de victimes et qui affiche la somme que le chasseur doit débourser.


def amende(p,c,v,a):
    points_perdus = p+(c*3)+(v*5)*(a*10)
    return 200 * (points_perdus/100)

p = int(input("Combien de poules ?"))
c = int(input("Combien de chiens ?"))
v = int(input("Combien de vaches ?"))
a = int(input("Combien d'amis ?"))
print(f" Vous devez payer {amende(p,c,v,a)} euros")