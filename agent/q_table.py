from typing import List, Tuple


class QTable:
    def __init__(self) -> None:
        self.table = {}

    def get_q_values(self, state: Tuple[bool, ...]) -> List[float]:
        if state not in self.table:

            danger_left = state[0]
            danger_right = state[3]
            danger_up = state[6]
            danger_down = state[9]

            q_right = 0.0
            q_left = 0.0
            q_up = 0.0
            q_down = 0.0

            if danger_right:
                q_right = -100.0
            if danger_left:
                q_left = -100.0
            if danger_up:
                q_up = -100.0
            if danger_down:
                q_down = -100.0

            self.table[state] = [q_right, q_left, q_up, q_down]

        return self.table[state]

    def update(self, state: Tuple[bool, ...],
               action: int, value: float) -> None:
        self.table[state][action] = value
