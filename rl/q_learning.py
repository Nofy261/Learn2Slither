from agent.q_table import QTable


class QLearning:
    def __init__(self) -> None:

        self.learning_rate = 0.1
        self.gamma = 0.9

    def update(self, q_table: QTable, state: tuple, action: int,
               reward: float, next_state: tuple, game_over: bool) -> None:
        old_value = q_table.get_q_values(state)[action]
        if game_over:
            best_future = 0
        else:
            future_values = q_table.get_q_values(next_state)
            best_future = max(future_values)
        new_value = (old_value
                     + self.learning_rate
                     * (reward + self.gamma * best_future - old_value))
        q_table.update(state, action, new_value)
