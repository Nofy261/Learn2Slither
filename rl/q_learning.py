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