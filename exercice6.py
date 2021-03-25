#L'utilisateur donne un entier supérieur à 1 et le programme affiche, s'il y en a, tous ses diviseurs propres sans répétition ainsi que leur nombre. S'il n'y en a pas, il indique qu'il est premier. Par exemple :

#Sélectionnez
#Entrez un entier strictement positif : 12
#Diviseurs propres sans répétition de 12 : 2 3 4 6 (soit 4 diviseurs propres)
#Entrez un entier strictement positif : 13
#Diviseurs propres sans répétition de 13 : aucun ! Il est premier

while True :
    n = input("Entrer un entier strictement positif : ")
    try:
        n_int = int(n)
        diviseurs = []
        #print(str(len(diviseurs)))
        for i in range(2,n_int):
            if n_int%i == 0:
                diviseurs.append(i)
        if len(diviseurs) == 0:
            print(f"Diviseurs propres sans répétition de {n_int} : aucun ! Il est premier")
        elif len(diviseurs)>0:
            print(f"Diviseurs propres sans répétition de {n} : {str(diviseurs).strip('[]').replace(',',' ')} (soit {len(diviseurs)} diviseurs propres)")
    except ValueError:
        print("Pas un nombre")