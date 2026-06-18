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
        self.score = 0
        self.game_over = False  # etat de la partie est fini ou pas

    def reset(self):

        """ relance une nouvelle partie propre """

        self.board.reset()
        self.score = 0
        self.game_over = False

    """
    VErsion 1

    def move_snake(self, action):

        
        #juste déplacer la tête + suivre le corps
        #on gere le deplacement pure sans condition cad deplacement de une case du serpent
        
        #  position de la tete actuelle  
        head = self.board.snake[0] 
        x, y = head

        #convertir action -> direction (dx, dy)
        if action == 0:
            dx, dy = (1, 0)
        elif action == 1:
            dx, dy = (-1, 0)
        elif action == 2:
            dx, dy = (0, -1)
        elif action == 3:
            dx, dy = (0, 1)
        else:
            dx, dy = (0, 0)
        
        #calcul nouvelle tete new_x = x + dx et new_y = y + dy
        new_head = (x + dx, y + dy)
        
        #deplacer le snake
        self.board.snake.insert(0, new_head)
        self.board.snake.pop()
    """


    # Version amelioré a tester
    def move_snake(self, action):

        head_x, head_y = self.board.snake[0]

        directions = {
            0: (1, 0),   # droite
            1: (-1, 0),  # gauche
            2: (0, -1),  # haut
            3: (0, 1)    # bas
        }

        dx, dy = directions.get(action, (0, 0))

        new_head = (head_x + dx, head_y + dy)

        # mise à jour snake
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
            # snake grandit de +1 et o annule le pop du move_snake
            self.board.snake.append(self.board.snake[-1])
            #reward change
            self.reward = 1
            self.score += 1
            
            self.board.spawn_green_apples()

        elif head == self.board.red_apple:
            #supprimer pomme rouge
            self.board.red_apple = None
            #snake retrecit (déjà pop dans move_snake → on enlève encore 1)
            if len(self.board.snake) > 0:
                self.board.snake.pop()
            
            self.reward = -1
            
            #score optionnel A VERIFIER SI BESOIN OU paS 
            self.score -= 1

            if len(self.board.snake) == 0:
                self.game_over = True

            self.board.spawn_red_apple()
    

    # utils
    def look_direction(self, dx, dy):

        head_x, head_y = self.board.snake[0]
        vision = []

        x, y = head_x, head_y

        while True:
            x += dx
            y += dy

            if x < 0 or x >= self.board.width or y < 0 or y >= self.board.height:
                vision.append("W")
                break

            cell = self.board.grid[y][x]

            if cell == 0:
                vision.append("0")
            elif cell == "S":
                vision.append("S")
            elif cell == "G":
                vision.append("G")
            elif cell == "R":
                vision.append("R")
            elif cell == "H":
                vision.append("H")
            
        return vision


    def get_state(self):

        left = self.look_direction(-1, 0)
        right = self.look_direction(1, 0)
        up = self.look_direction(0, -1)
        down = self.look_direction(0, 1)

        return (left, right, up, down)

    #step = 1 mouvement + conséquences + retour info a l'agent
    #step = 1 actin -> consequesnces -> nouvel etat

    """
    #version 1 
    def step(self, action):

    #qd le snake fait une action , le game change aussi
    #step fournit les conséquences d’une action à l’agent, qui les utilise pour apprendre

        self.reward = 0
        # bouger snake
        self.move_snake(action)
        # vérifier collisions (peut finir le jeu)
        self.check_collision()
        # gérer pommes (modifie snake + reward partiel)
        self.handle_apples()
        # reward par défaut (cas "rien mangé")
        
        if self.reward == 0:
            self.reward = -0.01 #petit penalty temps
        
        self.board.update_grid()

        state = self.get_state()
        
        return state, self.reward, self.game_over
    """

    #version amelioré A TESTEr

    def step(self, action):

        # reset reward à chaque step
        self.reward = 0

        #  déplacer le snake
        self.move_snake(action)

        # vérifier collisions (mur + self)
        self.check_collision()

        # si game over → reward forte pénalité
        if self.game_over:
            self.reward = -10
            state = self.get_state()
            return state, self.reward, self.game_over

        # gérer les pommes (green / red + reward intermédiaire)
        self.handle_apples()

        #reward par défaut si rien ne s’est passé
        if self.reward == 0:
            self.reward = -0.01  # petit penalty de temps

        #mise à jour de la grille (pour vision)
        self.board.update_grid()

        # état observé par l’agent
        state = self.get_state()

        #retour RL standard
        return state, self.reward, self.game_over



    

#action = mouvement(cad le snkae va a gauche ou a droite ou en haut en bas)
#step() applique une action dans le jeu, met à jour l’état du monde,
#  et retourne le résultat pour l’apprentissage

