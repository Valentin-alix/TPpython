import math

produits = {}
produits[1] = {"Id": 1,"nom": "Banane", "prix": 4.0}
produits[2] = {"Id": 2, "nom": "Pomme", "prix": 2.0}
produits[3] = {"Id": 3, "nom": "Orange", "prix": 1.5}
produits[4] = {"Id": 4, "nom": "Poire", "prix": 3.0}

p = input("Saisir le nombre de produit\n")
p = int(p)

liste = []

def tab(p):
    while p>0:
        
        a = input("Saisir l'id du produit\n")
        a = float(a)
        b = input("Saisir une quantité\n")
        b = int(b)
        print("+---------------------------+-------+------------------+------------+\n")
        print("|           Nom             |  Prix |        Quantite  | Total HT   |\n")
        print("+---------------------------+-------+------------------+------------+\n")
        print("|",produits[a]["nom"],"                   |",produits[a]["prix"],"  |         ",b,"      |  ",produits[a]["prix"]*b)

        print("+---------------------------+-------+------------------+------------+\n")
        liste.append(b * produits[a]["prix"])
        
        p = p-1
        

tab(p)

k=0
for i in liste:
    k = k + i



def affichage(k):
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