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

import random

class Board:

    def __init__(self):
        self.width = 10 #largeur (x)
        self.height = 10 #longueur(y)
        self.grid = [ #list de ligne
            [0 for _ in range(self.width)] #on creer une ligne de 10cases remplit de 0
            for _ in range(self.height)    #on le repete 10fois
        ]
        self.snake = []
        self.green_apples = []
        self.red_apple = None


    def create_snake(self):

        """
            Crée un serpent de 3 cases placé aléatoirement sur la grille.
            Le serpent est stocké dans self.snake sous forme de liste de tuples (x, y).
            Le premier élément est la tête.
        """


        directions = [
            (1, 0), #droite x = 1
            (-1, 0), #gauche x = -1
            (0, 1), #bas y = 1
            (0, -1) #haut y = -1
        ]

        while True:
            #tete random (eviter les murs)
            x = random.randint(2, self.width - 3)
            y = random.randint(2, self.height - 3)

            #direction random 
            dx, dy = random.choice(directions)

            #construire le snake tete->corps->queue [Head, Body, Body]
            snake = [
                (x, y),
                (x - dx, y - dy),
                (x - 2*dx, y - 2*dy)
            ]

            #verifie que tout est dns la grille
            valid = True

            for sx, sy in snake:
                if sx < 0 or sx >= self.width or sy < 0 or sy >= self.height:
                    valid = False
                    break
            
            #si valide on garde le snkae
            if valid:
                self.snake = snake
                break

    #self.snake = [(5,5), (4,5), (3,5)]
    #self.snake[0] -> (5,5)
    #self.snake[1] -> (4,5)
    #self.snake[2] -> (3,5)
    #head = self.snake[0]
    #(x,y) = tuple = paire de valeur


    def spawn_green_apples(self):

        """ 
            Génère 2 pommes vertes à des positions aléatoires libres.
            Une position est libre si elle n'est pas occupée par le serpent
            ou par une autre pomme verte.
        """

        self.green_apples = []

    #on veut 2pommes
        while len(self.green_apples) < 2:
            
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

            #verif si la case est libre
            #if self.grid[y][x] == 0:
            if (x, y) not in self.snake and (x, y) not in self.green_apples:
                #verif le snake
                #if (x, y) not in self.snake:
                #    self.grid[y][x] = "G"
                    self.green_apples.append((x, y))


    def spawn_red_apple(self):

        """
        Génère 1 pomme rouge à une position aléatoire libre.
        Une position est libre si elle n'est pas occupée par le serpent
        ou par une pomme verte.
        """
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

            if (x, y) not in self.snake and (x, y) not in self.green_apples:
                self.red_apple = (x, y)
                break


    def reset(self):

        """ 
        Remet le plateau à zéro et replace tous les éléments.
        À appeler au début de chaque nouvelle partie.
        """

        self.grid = [
            [0 for _ in range(self.width)]
            for _ in range(self.height)
        ]

        self.snake = []
        self.green_apples = []
        self.red_apple = None

        self.create_snake()
        self.spawn_green_apples()
        self.spawn_red_apple()

#update_grid synchronise la représentation visuelle avec l’état réel du jeu

    def update_grid(self):

        """ 
        Reconstruit la grille à partir des positions actuelles
        du serpent et des pommes.
        H = tête, S = corps, G = pomme verte, R = pomme rouge, 0 = vide
        """
        
        # reset de la grille
        self.grid = [
            [0 for _ in range(self.width)]
            for _ in range(self.height)
        ]

        # placer le snake
        for i, (x, y) in enumerate(self.snake):
            if i == 0:
                self.grid[y][x] = "H"
            else:
                self.grid[y][x] = "S"

        # placer les green apples
        for x, y in self.green_apples:
            self.grid[y][x] = "G"

        # placer la red apple
        if self.red_apple:
            x, y = self.red_apple
            self.grid[y][x] = "R"



#step(action) -> move() -> update_grid()

