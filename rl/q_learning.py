#formule de Bellamn 
#-> update q-values

#nouvelle_valeur = ancienne_valeur + learning_rate × (reward + gamma × meilleure_valeur_future - ancienne_valeur)

#def update(q_table, state, action, reward, next_state, learning_rate, gamma):
#   old_value = ...         # récupère l'ancienne valeur dans la q_table
#    future_values = ...     # récupère les valeurs du prochain état
#    best_future = ...       # prend la meilleure valeur future
#    new_value = ...         # applique la formule de Bellman
#    q_table.update(...)     # met à jour la q_table



class QLearning:
    def __init__(self):

        self.learning_rate = 0.1
        self.gamma = 0.9

    def update(self, q_table, state, action, reward, next_state):
        old_value = q_table.get_q_values(state)[action]
        future_values = q_table.get_q_values(next_state)
        best_future = max(future_values)
        new_value = old_value + self.learning_rate * (reward + self.gamma * best_future - old_value)
        q_table.update(state, action, new_value)

    
    #update reçoit :
        #state — où le serpent était
        #action — ce qu'il a fait
        #reward — ce qu'il a gagné/perdu
        #next_state — où il est maintenant

        # formule de bellman 
        #nouvelle_valeur = 2.1 + 0.1 × (1.45 - 2.1)
        #2.1 → ce qu'on pensait que ce pas valait avant de le faire
        #1.45 → ce que ce pas vaut vraiment (reward + gamma × best_future)
        #(1.45 - 2.1) → l'erreur qu'on a faite, on s'était trompé de -0.65
        #0.1 → on ne corrige que 10% de cette erreur, petit à petit
        #nouvelle_valeur → la valeur corrigée qu'on stocke dans la Q-table
        #En une phrase :
        #"Je pensais que ce pas valait 2.1, en réalité il vaut 1.45, je me suis trompé de -0.65,"
        #"donc je corrige 10% de cette erreur et je mets à jour ma Q-table avec 2.035."