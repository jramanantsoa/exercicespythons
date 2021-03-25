#L'utilisateur donne un entier positif et le programme annonce combien de fois de suite cet entier est divisible par 2.
n = input("Entrer un nb entier positif")
try:
    n_int = int(n)
    if n_int < 0:
        print("Entrer un nb positif")
        exit()
    else:
        divisible = 0
        while n_int%2==0:
            n_int=n_int/2
            divisible+=1
    print(f"Le nb {n} est divisible {divisible} fois par 2")
except ValueError:
    print("Pas correct")