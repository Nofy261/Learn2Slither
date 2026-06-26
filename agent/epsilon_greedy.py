
# decide parfois random (exploration) 
# parfois  exploitation 
# epsilon = 0.1  →  10% exploration / 90% exploitation
# epsilon = 0.9  →  90% exploration / 10% exploitation

# Au début du training → epsilon élevé (beaucoup d'exploration)
# Avec le temps → epsilon diminue (de plus en plus d'exploitation)

import random

class EpsilonGreedy:
    def __init__(self):
        self.epsilon = 0.9
        self.epsilon_min = 0.1
        self.epsilon_decay = 0.995

    def choose_action(self, state, q_table):

        """ retourne entre 0 et 3 cad l'action choisit gauche droite etc..."""

        rand = random.random() #  génère un nombre entre 0 et 1
        if rand < self.epsilon: #est ce que le nbre est tombé ds la zone d exploration
            return random.randint(0, 3) #choisit une action au hasard 
        else:
            values = q_table.get_q_values(state)
            return values.index(max(values)) #on prend le +grand nbre dnas qtable et retourne sa position et non sa valeur

    def reduce_epsilon(self): 
        self.epsilon = self.epsilon * self.epsilon_decay
        if self.epsilon < self.epsilon_min:
            self.epsilon = self.epsilon_min
