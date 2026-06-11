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
# class permet de regrouper tout dnas un seul objet

class Board:

    def __init__(self):
        self.width = 10 #largeur (x)
        self.height = 10 #longueur(y)
        self.grid = []
        for _ in range(self.height):
            row = []
            for _ in range(self.width):
                row.append(0)
            self.grid.append(row)




    # parcourir les lignes 
    # parcourir les colonnes 
    # grid[y][x]
    # grid[0][0] = "W"
    # grid[0][1] = 'W'
    # parcourir x -> remplir la premiere ligne de W

    #def create_walls(self):
    #    for x in range(self.width):
    #        self.grid[0][x] = 'W'
    #        self.grid[self.height - 1][x] = 'W'
    #    for y in range(self.height):
    #        self.grid[y][0] = 'W'
     #       self.grid[y][self.width - 1] = 'W'


    def create_walls(self):
        for y in range(self.height):
            for x in range(self.width):
                if y == 0 or y == self.height - 1:
                    self.grid[y][x] = 'W'
                elif x == 0 or x == self.width - 1:
                    self.grid[y][x] = 'W'

    def create_snake(self):
        

