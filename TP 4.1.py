import math

produits = {}
produits[1] = {"Id": 1,"nom": "Banane", "prix": 4.0}
produits[2] = {"Id": 2, "nom": "Pomme", "prix": 2.0}
produits[3] = {"Id": 3, "nom": "Orange", "prix": 1.5}
produits[4] = {"Id": 4, "nom": "Poire", "prix": 3.0}
try : 
    p = input("Saisir le nombre de produit\n")
    p = int(p)
    
    k = 0

    while p>0:
        a = input("Saisir l'id du produit\n")
        a = float(a)
        b = input("Saisir une quantité\n")
        b = int(b)
        k = k + produits[a]["prix"]
        print("+---------------------------+-------+------------------+------------+\n")
        print("|           Nom             |  Prix |        Quantite  | Total HT   |\n")
        print("+---------------------------+-------+------------------+------------+\n")
        print("|",produits[a]["nom"],"|",produits[a]["prix"])
    
        print("+---------------------------+-------+------------------+------------+\n")
        p = p-1
        if p == 0 :
            k = k * b  
    
    print("Sous-total HT :", k)
    r = 0
    if k > 200 :
        r = k*0.05 
        k = k*0.95
    print ("Remise 5% :",round (r,2))
    print ("Total HT :", round (k,2))
    k = k*1.20
    
    print ("Total TTC :", round (k,2))

except ValueError :
    print("Erreur d'entrée")