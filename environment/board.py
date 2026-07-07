import random


class Board:

    def __init__(self) -> None:
        self.width = 10
        self.height = 10
        self.snake = []
        self.green_apples = []
        self.red_apple = None

    def create_snake(self) -> None:

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while True:

            x = random.randint(2, self.width - 3)
            y = random.randint(2, self.height - 3)

            dx, dy = random.choice(directions)

            snake = [
                (x, y),
                (x - dx, y - dy),
                (x - 2*dx, y - 2*dy)
            ]

            valid = True

            for sx, sy in snake:
                if sx < 0 or sx >= self.width or sy < 0 or sy >= self.height:
                    valid = False
                    break

            if valid:
                self.snake = snake
                break

    def spawn_green_apples(self) -> None:

        self.green_apples = []

        while len(self.green_apples) < 2:

            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

            if ((x, y) not in self.snake
                    and (x, y) not in self.green_apples
                    and (x, y) != self.red_apple):
                self.green_apples.append((x, y))

    def spawn_red_apple(self) -> None:
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

            if (x, y) not in self.snake and (x, y) not in self.green_apples:
                self.red_apple = (x, y)
                break

    def reset(self) -> None:

        self.snake = []
        self.green_apples = []
        self.red_apple = None

        self.create_snake()
        self.spawn_green_apples()
        self.spawn_red_apple()
