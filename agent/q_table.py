# la memoire de l'iA

# c est la ou l IA stocke son apprentissage 
# Q(state, action) = valeur 
# Ex : Q["state1"]["UP"] = 0.5



class QTable:
    def __init__(self):
        self.table = {} #dictionnaire vide au debut
        #creer directement la cle - valeur ensemble


    #def get_q_values(self, state):
    #    if state not in self.table:
    #        self.table[state] = [0, 0, 0, 0]
    #    return self.table[state]

    #TEST 
    def get_q_values(self, state):
        if state not in self.table:

        # On recupere le danger pour chaque direction
        # depuis l'etat (tuple de 12 booleens)
            danger_left  = state[0]
            danger_right = state[3]
            danger_up    = state[6]
            danger_down  = state[9]

        # Q-values = [droite, gauche, haut, bas]
        # Si la direction est dangereuse (mur ou corps) → -100
        # Sinon → 0 (le snake apprendra par experience)
            self.table[state] = [
                -100.0 if danger_right else 0.0,
                -100.0 if danger_left  else 0.0,
                -100.0 if danger_up    else 0.0,
                -100.0 if danger_down  else 0.0,
            ]

        return self.table[state]

    def update(self, state, action, value):
        self.table[state][action] = value
    #ici value c'est le resultat obtenu avec la formule de Bellman  






