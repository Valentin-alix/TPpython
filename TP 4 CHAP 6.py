import math

Piece = {}
Piece[0] = {"nom": "origine","type" : "base"}
Piece[1] = {"nom": "emfer", "type": "prison"}
Piece[2] = {"nom": "gardesal", "type": "salle de garde"}
Piece[3] = {"nom": "salleamanger", "type": "cuisine"}
Piece[4] = {"nom": "chamber", "type": "chambre"}

class Personnage :
    pdv = 10
    salle = Piece[0]
    
    
print (Piece.keys())

"""for valeur in Piece.keys():
    print (valeur)"""