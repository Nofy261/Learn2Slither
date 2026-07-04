from typing import Tuple
from agent.q_table import QTable
import random

class EpsilonGreedy:
    def __init__(self) -> None:
        self.epsilon = 1.0

    def choose_action(self, state: Tuple[bool, ...], q_table: QTable) -> int:

        """ retourne entre 0 et 3 cad l'action choisit gauche droite etc..."""

        rand = random.random()
        if rand < self.epsilon:
            return random.randint(0, 3)
        else:
            values = q_table.get_q_values(state)
            return values.index(max(values))

    def reduce_epsilon(self, session: int, sessions: int) -> None:
        self.epsilon = max(0.05, 1.0 - (session / sessions) * 3)