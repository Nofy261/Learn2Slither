
# (le cerveau) fait : 
#le cerveau a besoin de ses 3 outils pour fonctionner :
#QTable → pour stocker
#QLearning → pour mettre à jour
#EpsilonGreedy → pour choisir


from agent.q_table import QTable
from agent.epsilon_greedy import EpsilonGreedy
from rl.q_learning import QLearning

class QAgent:

    def __init__(self):
        self.q_table = QTable()
        self.q_learning = QLearning()
        self.epsilon_greedy = EpsilonGreedy()

    
    def choose_action(self, state) -> int:
        action = self.epsilon_greedy.choose_action(state, self.q_table)
        return action


    def learn(self, state, action, reward, next_state, game_over) -> None:
        self.q_learning.update(self.q_table, state, action , reward, next_state, game_over)

    
    def end_session(self, session, sessions) -> None:
        self.epsilon_greedy.reduce_epsilon(session, sessions)
        
