#le cerveau de l'environnement 
# fait : state actuel -> 

#state actuel (board + snake)
#       ↓
#action de l’agent
#       ↓
#update snake
#       ↓
#update board
#     ↓
#collision ?
#      ↓
#reward
#       ↓
#next_state



#les regles, collisions, rewards

# appeler snake + board ensemble
# aplliquer une action
# calcul reward , detecter game over

#reset partie
#step action
#return : next_state, reward, done

# ce fichier game.py gere :
#lancer une partie
#faire avancer le jeu (step)
#détecter game over
#appeler reset()
#gérer la boucle d’entraînement RL

#les donnees de la partie
#game représente : une partie complète de Snake qui peut tourner,
#avancer, finir et recommencer

# Une partie de jeu = 
# --> Etat du jeu : board - score - etat:game over ou non
# --> La logique : bouger snake - gerer collision - manger les pommes
#     calcluer reward => step(action)
# --> Le reset(nouvelle partie) : Qd gameOver -> recreer snake,pommes,scores
#       => reset()
# --> Interaction avec l'agent
# Le jeu doit pouvoir :
#   recevoir une action (gauche, droite, haut, bas)
#   répondre avec :
#       nouvel état - reward - done
# Observation pour RL : le game doit fournir ce que l agent voit => get_state()

# Fichier qui decrit ce qui se passe quand on joue (regle + evolution du board a chaque action)

from environment.board import Board

class Game:
    def __init__(self):

        """ on initialise le jeu """

        self.board = Board()
        self.game_over = False  # etat de la partie est fini ou pas
        self.reward = 0
        self.reset() # AJOUT POUR TEST

    def reset(self):

        """ relance une nouvelle partie propre """

        self.board.reset()
        self.game_over = False
        self.reward = 0

    def move_snake(self, action):
        head_x, head_y = self.board.snake[0]
        directions = {
            0: (1, 0), #droite
            1: (-1, 0), #gauche
            2: (0, -1), #haut
            3: (0, 1) #bas
        }

        dx, dy = directions[action]
        new_head = (head_x + dx, head_y + dy)
        self.board.snake.insert(0, new_head)
        self.board.snake.pop()



    def check_collision(self):
        head = self.board.snake[0]
        x, y = head

        #verif collison avec le mur
        if x < 0 or x >= self.board.width or y < 0 or y >= self.board.height:
            self.game_over = True
            self.reward = -10
            return
        
        #Vérif collision avec le corps du snake
        if head in self.board.snake[1:]:
            self.game_over = True
            self.reward = -10
            return


    def handle_apples(self):

        """ on verifie si la tete du snake est sur une pomme, et ce qui va se passer ensuite
            gestion des conséquences des collisions avec les objets
        """

        head = self.board.snake[0]
    
        if head in self.board.green_apples:
            #on enleve la pomme mangé
            self.board.green_apples.remove(head)
            self.board.snake.append(self.board.snake[-1])
            self.reward = 1
            self.board.spawn_green_apples()
            

        elif head == self.board.red_apple:
            #supprimer pomme rouge
            self.board.red_apple = None
            if len(self.board.snake) > 0:
                self.board.snake.pop()
            self.reward = -1
            
            if len(self.board.snake) == 0:
                self.game_over = True
                return
            
            self.board.spawn_red_apple()
    

    def look_direction(self, dx, dy):
        head_x, head_y = self.board.snake[0]
        x, y = head_x, head_y

        while True:
            x += dx
            y += dy

            if x < 0 or x >= self.board.width or y < 0 or y >= self.board.height:
                return "W"
            if (x, y) in self.board.snake:
                return "S"
            if (x, y) in self.board.green_apples:
                return "G"
            if (x, y) == self.board.red_apple:
                return "R"

            #return "0" # TEST A REMETRRE
        

    def encode_direction(self, cell):

        """
        Transforme la vision brute d’une direction en informations simples pour l’agent RL.
        Pour une direction donnée (liste de cases dans l’ordre de vision du snake),
        on extrait 3 informations essentielles :
        - danger : True si un mur (W) ou le corps du snake (S) est détecté
        - green : True si une pomme verte (G) est visible avant tout obstacle
        - red : True si une pomme rouge (R) est visible avant tout obstacle
        Cette fonction permet de simplifier l’observation pour l’agent afin de
        faciliter l’apprentissage par renforcement avec un vecteur de taille fixe.
        """

        danger = cell in ("W", "S")
        green = (cell == "G")
        red = (cell == "R")
       
        return (danger, green, red)



    def get_state(self):

        left = self.look_direction(-1, 0)
        right = self.look_direction(1, 0)
        up = self.look_direction(0, -1)
        down = self.look_direction(0, 1)

        left_state = self.encode_direction(left)
        right_state = self.encode_direction(right)
        up_state = self.encode_direction(up)
        down_state = self.encode_direction(down)

        return left_state + right_state + up_state + down_state


    def step(self, action):

        self.reward = 0

        self.move_snake(action)
        self.check_collision()
        self.handle_apples()
        self.state = self.get_state()
        return self.state, self.reward, self.game_over



    def get_vision_line(self, dx, dy):
        head_x, head_y = self.board.snake[0]
        x, y = head_x, head_y
        vision_line = []

        while True:
            x += dx
            y += dy

            if x < 0 or x >= self.board.width or y < 0 or y >= self.board.height:
                vision_line.append("W")
                break
            if (x, y) in self.board.snake:
                vision_line.append("S")
                break
            if (x, y) in self.board.green_apples:
                vision_line.append("G")
                break
            if (x, y) == self.board.red_apple:
                vision_line.append("R")
                break
            else:
                vision_line.append("0")
        return vision_line









   
#action = mouvement(cad le snkae va a gauche ou a droite ou en haut en bas)
#step() applique une action dans le jeu, met à jour l’état du monde,
#  et retourne le résultat pour l’apprentissage

