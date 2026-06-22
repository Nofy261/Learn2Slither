
from environment.game import Game
import time
import random



def print_grid(grid):
    for line in grid:
        print(" ".join(str(cell) for cell in line))
    print("\n" + "-" * 30 + "\n")


def main():

    game = Game()
    game.reset()

    while not game.game_over:

        # action aléatoire (agent baseline)
        action = random.randint(0, 3)

        state, reward, done = game.step(action)

        # affichage grille
        print_grid(game.board.grid)

        print("Reward:", reward)
        print("Game Over:", done)

        time.sleep(0.3)  # ralentir pour voir le jeu

    print("FIN DU JEU")


if __name__ == "__main__":
    main()






"""
for line in game.board.grid:
    print(" ".join(str(x) for x in line))"""