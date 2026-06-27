
from visualization.display import Display
from environment.board import Board
from environment.game import Game
from agent.q_agent import QAgent
import argparse
from utils.saver import load, save
from utils.logger import print_state


def main():

    game = Game()  
    q_agent = QAgent()
    

    parser = argparse.ArgumentParser()

    parser.add_argument("-sessions", type=int, default=100)
    parser.add_argument("-save", type=str)
    parser.add_argument("-load", type=str)
    parser.add_argument("-visual", type=str, default="on")
    parser.add_argument("-dontlearn", action="store_true")
    parser.add_argument("-step-by-step", action="store_true")

    args = parser.parse_args()

    if args.visual == "on":
        display = Display(game.board)
    
    if args.load:
        q_agent.q_table.table = load(args.load)

    for session in range(args.sessions):
        game.reset()
        state = game.get_state()

        while not game.game_over:
            action = q_agent.choose_action(state)
            print_state(game, action)
            next_state, reward, game_over = game.step(action)
            if not args.dontlearn:
                q_agent.learn(state, action, reward, next_state)

            if args.visual == "on":
                display.draw()
                display.handle_events()
                if args.step_by_step:
                    display.wait_for_keypress()
                else:
                    display.clock.tick(10)
            state = next_state

        q_agent.end_session()

        if session == 0:
            save(q_agent.q_table, "models/model_1.txt")
        if session == 9:
            save(q_agent.q_table, "models/model_10.txt")
        if session == 99:
            save(q_agent.q_table, "models/model_100.txt")

    if args.save:
        save(q_agent.q_table, args.save)




if __name__ == "__main__":
    main()



BUGG A TESTER : python main.py -sessions 2 -visual on -step-by-step


#./snake -sessions 10 -save models/10sess.txt -visual off
#./snake -visual on -load models/100sess.txt -sessions 10 -dontlearn -step-by-step
#Load trained model from models/100sess.txt
#./snake -visual on -load models/1000sess.tx


#-sessions, -save, -load, -visual, -dontlearn, -step-by-step.