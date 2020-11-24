import math

produits = {}
produits[1] = {"Id": 1,"nom": "Banane", "prix": 4.0}
produits[2] = {"Id": 2, "nom": "Pomme", "prix": 2.0}
produits[3] = {"Id": 3, "nom": "Orange", "prix": 1.5}
produits[4] = {"Id": 4, "nom": "Poire", "prix": 3.0}

try :
    p = input("Saisir le nombre de produit\n")
    p = int(p)
    h = p
except :
    print("Erreur de saisie du nombre de produit")

else :

    liste = []
    temp =  []
    temp2 = []
    temp3 = []
    temp4 = []

    while p>0:
        try :
            a = input("Saisir l'id du produit\n")
            a = int(a)
            b = input("Saisir une quantité\n")
            b = int(b)
        except :
            print("Erreur de saisie de l'id ou de la quantité")
        else :
            temp.append(produits[a]["nom"])
            temp2.append(produits[a]["prix"])
            temp3.append(b)
            temp4.append(produits[a]["prix"]*b)
            a = float(a)    
            liste.append(b * produits[a]["prix"])

            p = p-1




    k=0
    for i in liste:
        k = k + i


    def affichage(k):

        print("+---------------------------+-------+------------------+------------+\n")
        print("|           Nom             |  Prix |        Quantite  | Total HT   |\n")
        print("+---------------------------+-------+------------------+------------+\n")
        for i in range(h):
            print("          ",temp[i],"            ",temp2[i],"           ",temp3[i],"          ",temp4[i])
        print("+---------------------------+-------+------------------+------------+\n")

        print("Sous-total HT :", k)
        r = 0
        if k > 200 :
            r = k*0.05 
            k = k*0.95
        print ("Remise 5% :",round (r,2))
        print ("Total HT :", round (k,2))
        k = k*1.20

        print ("Total TTC :", round (k,2))

    affichage(k)