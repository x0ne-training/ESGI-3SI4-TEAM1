import pygame
import os

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu plateforme scrolling")

background_color = (135, 206, 235)
ground_color = (0, 255, 0)

GROUND_Y = HEIGHT - 50
PLAYER_SPEED = 5
GRAVITY = 1
JUMP_STRENGTH = -15
ANIMATION_DELAY = 5

def load_images_from_folder(folder):
    if not os.path.exists(folder):
        print(f"❌ Dossier introuvable : {folder}")
        return []

    images = []
    for filename in sorted(os.listdir(folder)):
        if filename.endswith(".png"):
            path = os.path.join(folder, filename)
            try:
                image = pygame.image.load(path).convert_alpha()
                image = pygame.transform.scale(image, (50, 50))
                images.append(image)
            except Exception as e:
                print(f"⚠️ Erreur chargement {filename}: {e}")
    return images

idle_images = load_images_from_folder(r"c:\Users\idimi\Documents\Codage\Python\ESGI-3SI4-TEAM1\jeux\jeux-plateforme2D\idle")
run_images = load_images_from_folder(r"c:\Users\idimi\Documents\Codage\Python\ESGI-3SI4-TEAM1\jeux\jeux-plateforme2D\run")
jump_images = load_images_from_folder(r"c:\Users\idimi\Documents\Codage\Python\ESGI-3SI4-TEAM1\jeux\jeux-plateforme2D\jump")
fall_images = load_images_from_folder(r"c:\Users\idimi\Documents\Codage\Python\ESGI-3SI4-TEAM1\jeux\jeux-plateforme2D\fall")

print(f"Idle: {len(idle_images)} Run: {len(run_images)} Jump: {len(jump_images)} Fall: {len(fall_images)}")

class Platform:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface, scroll_x):
        pygame.draw.rect(surface, (139, 69, 19), self.rect.move(-scroll_x, 0))

    def get_rect(self, scroll_x):
        return self.rect.move(-scroll_x, 0)

platforms = [
    Platform(0, GROUND_Y, 2000, 50),
    Platform(300, GROUND_Y - 100, 100, 20),
    Platform(600, GROUND_Y - 150, 150, 20),
    Platform(900, GROUND_Y - 200, 100, 20),
    Platform(1300, GROUND_Y - 120, 200, 20),
]

player_x = 100
player_y = GROUND_Y - 50
player_velocity_x = 0
player_velocity_y = 0
on_ground = False

frame_index = 0
animation_counter = 0
current_animation = idle_images
facing_right = True

scroll_x = 0

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    moving = False
    player_velocity_x = 0

    if keys[pygame.K_LEFT]:
        player_velocity_x = -PLAYER_SPEED
        moving = True
        facing_right = False
    if keys[pygame.K_RIGHT]:
        player_velocity_x = PLAYER_SPEED
        moving = True
        facing_right = True
    if keys[pygame.K_SPACE] and on_ground:
        player_velocity_y = JUMP_STRENGTH
        on_ground = False

    player_x += player_velocity_x
    player_rect = pygame.Rect(player_x, player_y, 50, 50)

    for platform in platforms:
        plat_rect = platform.get_rect(scroll_x)
        if player_rect.colliderect(plat_rect):
            if player_velocity_x > 0:
                player_x = plat_rect.left - 50
            elif player_velocity_x < 0:
                player_x = plat_rect.right
            player_rect.x = player_x

    player_x = max(0, min(player_x, 2000 - 50))
    player_rect.x = player_x

    player_velocity_y += GRAVITY
    player_y += player_velocity_y
    player_rect.y = player_y

    on_ground = False
    for platform in platforms:
        plat_rect = platform.get_rect(scroll_x)
        if player_rect.colliderect(plat_rect):
            if player_velocity_y > 0 and player_rect.bottom - player_velocity_y <= plat_rect.top:
                player_y = plat_rect.top - 50
                player_velocity_y = 0
                on_ground = True
                player_rect.y = player_y

    if player_y > HEIGHT + 100:
        player_x = 100
        player_y = GROUND_Y - 50
        player_velocity_y = 0
        player_rect.x = player_x
        player_rect.y = player_y

    if player_x - scroll_x > WIDTH * 0.6:
        scroll_x = player_x - WIDTH * 0.6
    elif player_x - scroll_x < WIDTH * 0.3:
        scroll_x = player_x - WIDTH * 0.3
    scroll_x = max(0, scroll_x)

    if not on_ground:
        if player_velocity_y < 0:
            current_animation = jump_images
        else:
            current_animation = fall_images
    else:
        current_animation = run_images if moving else idle_images

    if len(current_animation) == 0:
        current_frame = pygame.Surface((50, 50))
        current_frame.fill((255, 0, 0))
    else:
        animation_counter += 1
        if animation_counter >= ANIMATION_DELAY:
            animation_counter = 0
            frame_index = (frame_index + 1) % len(current_animation)
        frame_index %= len(current_animation)
        current_frame = current_animation[frame_index]
        if not facing_right: 
            current_frame = pygame.transform.flip(current_frame, True, False)

    screen.fill(background_color)

    for platform in platforms:
        platform.draw(screen, scroll_x)

    screen.blit(current_frame, (player_x - scroll_x, player_y))

    pygame.display.flip()

pygame.quit()
