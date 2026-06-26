
from visualization.display import Display
from environment.board import Board
from environment.game import Game
from agent.q_agent import QAgent


def main():
    game = Game()  
    q_agent = QAgent()
    display = Display(game.board)


    for _ in range(100):
        game.reset()
        state = game.get_state()

        while not game.game_over:
            action = q_agent.choose_action(state)
            next_state, reward, game_over = game.step(action)
            q_agent.learn(state, action, reward, next_state)
            display.draw()
            state = next_state
        q_agent.end_session()





if __name__ == "__main__":
    main()



