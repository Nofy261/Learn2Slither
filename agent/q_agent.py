from agent.q_table import QTable
from agent.epsilon_greedy import EpsilonGreedy
from rl.q_learning import QLearning
from typing import Tuple


class QAgent:

    def __init__(self) -> None:
        self.q_table = QTable()
        self.q_learning = QLearning()
        self.epsilon_greedy = EpsilonGreedy()

    def choose_action(self, state: Tuple[bool, ...]) -> int:
        action = self.epsilon_greedy.choose_action(state, self.q_table)
        return action

    def learn(self, state: tuple, action: int, reward: float,
              next_state: tuple, game_over: bool) -> None:
        self.q_learning.update(self.q_table, state, action,
                               reward, next_state, game_over)

    def end_session(self, session: int, sessions: int) -> None:
        self.epsilon_greedy.reduce_epsilon(session, sessions)
