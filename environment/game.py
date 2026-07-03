from typing import Tuple, List
from environment.board import Board


class Game:
    def __init__(self) -> None:
        """ on initialise le jeu """
        self.board = Board()
        self.game_over = False
        self.reward = 0
        self.reset()

    def reset(self) -> None:
        """ relance une nouvelle partie propre """
        self.board.reset()
        self.game_over = False
        self.reward = 0
        self.state = self.get_state()

    def check_collision(self) -> None:
        head = self.board.snake[0]
        x, y = head

        if x < 0 or x >= self.board.width or y < 0 or y >= self.board.height:
            self.game_over = True
            self.reward = -100
            return

        if head in self.board.snake[1:-1]:
            self.game_over = True
            self.reward = -100
            return

    def move_snake(self, action: int) -> None:
        head_x, head_y = self.board.snake[0]
        directions = {
            0: (1, 0),   # droite
            1: (-1, 0),  # gauche
            2: (0, -1),  # haut
            3: (0, 1)    # bas
        }

        dx, dy = directions[action]
        new_head = (head_x + dx, head_y + dy)
        self.board.snake.insert(0, new_head)
        self.check_collision()
        self.board.snake.pop()

    def handle_apples(self) -> None:
        """
        Verifie si la tete du snake est sur une pomme.
        Gestion des consequences des collisions avec les objets.
        """
        head = self.board.snake[0]

        if head in self.board.green_apples:
            # on enleve la pomme mangee
            self.board.green_apples.remove(head)
            self.board.snake.append(self.board.snake[-1])
            self.reward = 10
            self.board.spawn_green_apples()

        elif head == self.board.red_apple:
            # supprimer pomme rouge
            self.board.red_apple = None
            if len(self.board.snake) > 0:
                self.board.snake.pop()
            self.reward = -10

            if len(self.board.snake) == 0:
                self.game_over = True
                return

            self.board.spawn_red_apple()

    def get_vision_line(self, dx: int, dy: int) -> List[str]:
        head_x, head_y = self.board.snake[0]
        x, y = head_x, head_y
        vision_line = []

        while True:
            x += dx
            y += dy

            if (x < 0 or x >= self.board.width
                    or y < 0 or y >= self.board.height):
                vision_line.append("W")
                break
            if (x, y) in self.board.snake:
                vision_line.append("S")
            elif (x, y) in self.board.green_apples:
                vision_line.append("G")
            elif (x, y) == self.board.red_apple:
                vision_line.append("R")
            else:
                vision_line.append("0")
        return vision_line

    def look_direction(self, dx: int, dy: int) -> List[str]:
        """
        Retourne la liste de ce qu'on voit dans une direction.
        Caracteres : 'W' (mur), 'S' (corps), 'G' (pomme verte),
        'R' (pomme rouge), '0' (vide).
        """
        head_x, head_y = self.board.snake[0]
        x, y = head_x, head_y
        vision_line = []

        while True:
            x += dx
            y += dy

            if (x < 0 or x >= self.board.width
                    or y < 0 or y >= self.board.height):
                vision_line.append("W")
                break
            if (x, y) in self.board.snake[:-1]:
                vision_line.append("S")
            elif (x, y) in self.board.green_apples:
                vision_line.append("G")
            elif (x, y) == self.board.red_apple:
                vision_line.append("R")
            else:
                vision_line.append("0")

        return vision_line

    def encode_direction(self, vision_line: List[str]
                         ) -> Tuple[bool, bool, bool]:
        """
        Encode une liste de vision en 3 booleens : (danger, green, red).
        """
        danger = len(vision_line) > 0 and vision_line[0] in ('W', 'S')

        green = False
        for case in vision_line:
            if case in ('S', 'W'):
                break
            if case == 'G':
                green = True
                break

        red = False
        for case in vision_line:
            if case in ('S', 'W'):
                break
            if case == 'R':
                red = True
                break

        return (danger, green, red)

    def get_state(self) -> Tuple[bool, ...]:
        left = self.look_direction(-1, 0)
        right = self.look_direction(1, 0)
        up = self.look_direction(0, -1)
        down = self.look_direction(0, 1)

        left_state = self.encode_direction(left)
        right_state = self.encode_direction(right)
        up_state = self.encode_direction(up)
        down_state = self.encode_direction(down)
        return left_state + right_state + up_state + down_state

    def step(self, action: int) -> Tuple[Tuple[bool, ...], float, bool]:
        self.reward = 0
        self.move_snake(action)
        if not self.game_over:
            self.handle_apples()
        if not self.game_over and self.reward == 0:
            self.reward = -3
        if not self.game_over:
            self.state = self.get_state()
        return self.state, self.reward, self.game_over
