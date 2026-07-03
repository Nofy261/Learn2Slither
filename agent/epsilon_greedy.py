
# decide parfois random (exploration) 
# parfois  exploitation 
# epsilon = 0.1  →  10% exploration / 90% exploitation
# epsilon = 0.9  →  90% exploration / 10% exploitation

# Au début du training → epsilon élevé (beaucoup d'exploration)
# Avec le temps → epsilon diminue (de plus en plus d'exploitation)

import random

class EpsilonGreedy:
    def __init__(self):
        self.epsilon = 1.0

    def choose_action(self, state, q_table):

        """ retourne entre 0 et 3 cad l'action choisit gauche droite etc..."""

        rand = random.random()
        if rand < self.epsilon:
            return random.randint(0, 3)
        else:
            values = q_table.get_q_values(state)
            return values.index(max(values))

    def reduce_epsilon(self, session, sessions):
        self.epsilon = max(0.05, 1.0 - (session / sessions) * 3)