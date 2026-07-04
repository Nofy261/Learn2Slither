import random

class Board:

    def __init__(self) -> None:
        self.width = 10 #largeur (x)
        self.height = 10 #longueur(y)
        self.grid = [ #list de ligne
            [0 for _ in range(self.width)] #on creer une ligne de 10cases remplit de 0
            for _ in range(self.height)    #on le repete 10fois
        ]
        self.snake = []
        self.green_apples = []
        self.red_apple = None


    def create_snake(self) -> None:

        """
            Crée un serpent de 3 cases placé aléatoirement sur la grille.
            Le serpent est stocké dans self.snake sous forme de liste de tuples (x, y).
            Le premier élément est la tête.
        """

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
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

    def spawn_green_apples(self) -> None:

        """ 
            Génère 2 pommes vertes à des positions aléatoires libres.
            Une position est libre si elle n'est pas occupée par le serpent
            ou par une autre pomme verte.
        """

        self.green_apples = []

        while len(self.green_apples) < 2:
            
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

            if (x, y) not in self.snake and (x, y) not in self.green_apples:
                self.green_apples.append((x, y))


    def spawn_red_apple(self) -> None:

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


    def reset(self) -> None:

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

