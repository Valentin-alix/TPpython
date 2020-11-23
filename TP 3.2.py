p = input("Saisir le nombre de produit\n")
p = int(p)
i = p
while i>0:
    a = input("Saisir un prix hors taxe\n")
    a = float(a)
    b = input("Saisir une quantité\n")
    b = int(b)
    if a and b :
        if a > 0 and b > 0 :
            c = a*b*1.20
            print(c)

            if c > 200:
                c = c*0.95
                print(c)
    
        else :
            print("Erreur veuillez tapez une quantité et un prix positif")
    i = i-1

        
