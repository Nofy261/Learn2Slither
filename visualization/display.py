import pygame
from environment.board import Board

CELL_SIZE = 60
WHITE = (255, 255, 255)
GRAY  = (200, 200, 200)
BLUE  = (0, 0, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)


class Display:

    def __init__(self, board):
        pygame.init()
        self.board = board
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        

    def draw_grid(self):
        self.screen.fill(WHITE)
        for x in range(10):
            for y in range(10):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, GRAY, rect, 1)
        pygame.display.flip()


    def draw_snake(self):
        for (x, y) in self.board.snake:
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.screen, BLUE, rect)

    def draw_green_apples(self):
        for (x, y) in self.board.green_apples:
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.screen, GREEN, rect)
    

    def draw_red_apple(self):
        if self.board.red_apple:
            x, y = self.board.red_apple
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.screen, RED, rect)


    def draw(self):
        self.draw_grid()
        self.draw_snake()
        self.draw_green_apples()
        self.draw_red_apple()
        pygame.display.flip()

    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def wait_for_keypress(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    waiting = False
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    exit()