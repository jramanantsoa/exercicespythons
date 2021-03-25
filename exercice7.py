#Écrire un programme qui approxime par défaut la valeur de la constante mathématique e, pour n assez grand(56), en utilisant la formule :
#Pour cela, définissez la fonction factorielle et, dans votre programme principal, saisissez l'ordre n et affichez l'approximation correspondante de e.

def factorielle(n):
    fact = 1 
    for i in range(1,n+1):
        fact *=i
    return fact

n = input("n ? ")
try:
    n_int= int(n)
    e = 0.0
    for i in range(n_int):
        e = e+1/factorielle(i)
    print(str(e))
except ValueError:
    print("Pas un nombre")
