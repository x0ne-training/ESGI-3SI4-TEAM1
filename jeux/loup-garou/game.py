import pygame
from settings import *
from roles import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Loup Garou")
        self.clock = pygame.time.Clock()

        # Exemple de joueurs + rôles
        self.players = [
            {"name": "Alice", "role": LoupGarou()},
            {"name": "Bob", "role": Voyante()},
            {"name": "Claire", "role": Villageois()}
        ]

        self.font = pygame.font.SysFont("arial", 28)

    def draw_text(self, text, x, y):
        img = self.font.render(text, True, WHITE)
        self.screen.blit(img, (x, y))

    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(BLACK)

            # Affichage simple des joueurs et rôles
            y = 50
            for p in self.players:
                self.draw_text(f"{p['name']} : {p['role'].name}", 50, y)
                y += 40

            pygame.display.flip()

        pygame.quit()
