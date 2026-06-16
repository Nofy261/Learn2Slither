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

from environment.board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.score = 0
        self.done = False  # etat de la partie est fini ou pas

    def reset(self): #relance une nouvelle partie propre 
        self.board.reset()
        self.score = 0
        self.done = False

    #step = une action de l’agent + mise à jour du jeu +
    # retour de l’état et du reward”
    #step = 1 mouvement + conséquences + retour info a l'agent
    def step(self, action): #qd le snake fait une action , le game change aussi
        # 1. bouger snake
        # 2. vérifier collisions
        # 3. gérer pommes
        # 4. calcul reward
        # 5. vérifier game over

        return state, reward, self.done
    #step fournit les conséquences d’une action à l’agent, qui les utilise pour apprendre

    def get_state(self):
        return self.board  # ou state_builder plus tard
    

#action = mouvement(cad le snkae va a gauche ou a droite ou en haut en bas)
#step() applique une action dans le jeu, met à jour l’état du monde,
#  et retourne le résultat pour l’apprentissage

