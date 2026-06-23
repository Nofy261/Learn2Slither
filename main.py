
from visualization.display import Display
from environment.board import Board
from environment.game import Game

def main():
    game = Game() 
    game.reset()  
    display = Display(game.board)


    while not game.game_over:
        display.handle_events()
        action = 3 #test
        game.step(action)
        display.draw()

    while True:
        display.handle_events()

if __name__ == "__main__":
    main()



