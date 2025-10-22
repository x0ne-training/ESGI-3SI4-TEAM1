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

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    WINDOW.fill(BLACK)
    pygame.display.flip()
    CLOCK.tick(10)

pygame.quit()
sys.exit()
