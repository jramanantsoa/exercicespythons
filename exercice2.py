#Une boucle while : entrez un prix HT (entrez o pour terminer) et affichez sa valeur TTC.
prix_ht = input("Prix HT : ")
while prix_ht !="o":
    if not prix_ht.isdigit() and prix_ht !="o":
        print("Pas compris.")
        break
    print("Prix TTC : "+str(float(prix_ht)*1.196))
    prix_ht = input("Prix HT : (o pour sortir)")
print("Bye")