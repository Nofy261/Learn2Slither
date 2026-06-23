
from visualization.display import Display
from environment.board import Board

def main():
    board = Board()
    board.reset()
    display = Display(board)
    display.run()



if __name__ == "__main__":
    main()



