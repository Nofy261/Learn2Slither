#affiche dans le terminal :
#La vision — ce que le snake voit dans les 4 directions avant de choisir
#L'action — la direction qu'il a choisie


ACTIONS = {0: "RIGHT", 1: "LEFT", 2: "UP", 3: "DOWN"}


def print_state(game, action):
    up = list(reversed(game.get_vision_line(0, -1)))
    down = game.get_vision_line(0, 1)
    left = list(reversed(game.get_vision_line(-1, 0)))
    right = game.get_vision_line(1, 0)

    pad = len(left)

    print()
    for cell in up:
        print(" " * pad + cell)
    print("".join(left) + "H" + "".join(right))
    for cell in down:
        print(" " * pad + cell)

    print()
    print(ACTIONS.get(action, str(action)))


    #!! A REFAIRE CAR BUGG 