import pygame
import sys
import random

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

    def eat(self, food):
        if self.body[0] == food.position:
            self.body.append(self.body[-1])
            return True
        return False

    def check_collision(self):
        head = self.body[0]
        # Collision avec les murs
        if (head[0] < 0 or head[0] >= GRID_WIDTH or 
            head[1] < 0 or head[1] >= GRID_HEIGHT):
            return True
        # Collision avec soi-même
        if head in self.body[1:]:
            return True
        return False




class Food:
    def __init__(self):
        self.position = self.random_position()
    
    def random_position(self):
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        return (x, y)
    
    def draw(self, surface):
        rect = pygame.Rect(self.position[0] * CELL_SIZE,
                          self.position[1] * CELL_SIZE,
                          CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, RED, rect)

food = Food()
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

            if snake.eat(food):
                food.position = food.random_position()

            if snake.check_collision():
                running = False

        if event.type == pygame.QUIT:
            running = False
    
    WINDOW.fill(BLACK)
    snake.move()
    snake.draw(WINDOW)
    food.draw(WINDOW)
    pygame.display.flip()
    CLOCK.tick(10)

pygame.quit()
sys.exit()
