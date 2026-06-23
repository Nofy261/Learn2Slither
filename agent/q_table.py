# la memoire de l'iA

# c est la ou l IA stocke son apprentissage 
# Q(state, action) = valeur 
# Ex : Q["state1"]["UP"] = 0.5



class QTable:
    def __init__(self):
        self.table = {} #dictionnaire de nom table vide au debut
        #creer directement la cle - valeur ensemble



    def get_q_values(self, state):
        if state not in self.table:
            self.table[state] = [0, 0, 0, 0]
        return self.table[state]


    def update(self, state, action, value):
        self.table[state][action] = value
    #ici value c'est le resultat obtenu avec la formule de Bellman  

    
     
