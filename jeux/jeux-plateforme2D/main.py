import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de plateforme 2D")

background_color = (135, 206, 235)
player_color = (255, 0, 0)
ground_color = (0, 255, 0)

player_width, player_height = 50, 50
player_x = 100
player_y = HEIGHT - player_height - 50 
player_velocity_x = 0
player_velocity_y = 0
player_speed = 5
jump_strength = -15
gravity = 1
on_ground = True

ground_y = HEIGHT - 50

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player_velocity_x = 0
    if keys[pygame.K_LEFT]:
        player_velocity_x = -player_speed
    if keys[pygame.K_RIGHT]:
        player_velocity_x = player_speed
    if keys[pygame.K_SPACE] and on_ground:
        player_velocity_y = jump_strength
        on_ground = False

    player_velocity_y += gravity

    player_x += player_velocity_x
    player_y += player_velocity_y

    if player_y + player_height >= ground_y:
        player_y = ground_y - player_height
        player_velocity_y = 0
        on_ground = True

    screen.fill(background_color)
    pygame.draw.rect(screen, ground_color, (0, ground_y, WIDTH, 50))  # Sol
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))  # Joueur

    pygame.display.flip()

pygame.quit()
