#le monde du serpent : decrit l'etat actuel du monde

#la grille 10*10
# les positions des pommes , murs, cases vides, etat global du jeu
#murs 
# creer la grille
#palcer le snake , les pommes
# verif collisions
#mettre a jour le board , savoir si une case est vode ou ocuupé
# affiche ou return le grille

#Stocker le monde
#Vérifier collisions
#Mettre à jour le snake
#Gérer les pommes

#initialisation du board

class Board:

    def __init__(self):
        self.width = 10 #largeur (x)
        self.height = 10 #longueur(y)
