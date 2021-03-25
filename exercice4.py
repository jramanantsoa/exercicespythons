#L'utilisateur donne un entier positif n et le programme affiche PAIR s'il est divisible par 2, IMPAIR sinon.
n = input("Entrer un nombre")
try:
    n_int = int(n)
    if n_int%2==0:
        print("Pair")
    else:
        print("impair")
except ValueError:
    print("Ce n'est pas un nombre")