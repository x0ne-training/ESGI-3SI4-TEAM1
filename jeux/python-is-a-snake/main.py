import pygame
import sys

pygame.init()

# Constantes
WIDTH, HEIGHT = 600, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
CLOCK = pygame.time.Clock()

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Paramètres du jeu
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE


class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
    
    def draw(self, surface):
        for segment in self.body:
            rect = pygame.Rect(segment[0] * CELL_SIZE, 
                             segment[1] * CELL_SIZE, 
                             CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, GREEN, rect)

    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        self.body.insert(0, new_head)
        self.body.pop()

snake = Snake()


# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != (0, 1):
                snake.direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
                snake.direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
                snake.direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                snake.direction = (1, 0)
        if event.type == pygame.QUIT:
            running = False
    
    WINDOW.fill(BLACK)
    snake.move()
    snake.draw(WINDOW)
    pygame.display.flip()
    CLOCK.tick(10)

pygame.quit()
sys.exit()
