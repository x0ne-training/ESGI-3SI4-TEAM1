import pygame
import os

pygame.init()

# --- CONFIGURATION ---
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu plateforme scrolling")

BACKGROUND_COLOR = (135, 206, 235)
GROUND_Y = HEIGHT - 50
PLAYER_SPEED = 5
GRAVITY = 1
JUMP_STRENGTH = -15
ANIMATION_DELAY = 5

# --- DASH CONFIG ---
DASH_SPEED = 12      # vitesse raisonnable
DASH_DURATION = 12    # frames
DASH_COOLDOWN = 60    # frames (1 sec à 60 FPS)

# --- FONCTION DE CHARGEMENT ---
def load_images_from_folder(folder, size=(50, 50)):
    if not os.path.exists(folder):
        print(f"❌ Dossier introuvable : {folder}")
        return []
    images = []
    for filename in sorted(os.listdir(folder)):
        if filename.endswith(".png"):
            path = os.path.join(folder, filename)
            try:
                img = pygame.image.load(path).convert_alpha()
                img = pygame.transform.scale(img, size)
                images.append(img)
            except Exception as e:
                print(f"⚠️ Erreur chargement {filename}: {e}")
    return images

# --- CHARGEMENT DES ANIMATIONS ---
base_path = r"c:\Users\idimi\Documents\Codage\Python\ESGI-3SI4-TEAM1\jeux\jeux-plateforme2D"
idle_images = load_images_from_folder(os.path.join(base_path, "idle"))
run_images = load_images_from_folder(os.path.join(base_path, "run"))
jump_images = load_images_from_folder(os.path.join(base_path, "jump"))
fall_images = load_images_from_folder(os.path.join(base_path, "fall"))
attack_images = load_images_from_folder(os.path.join(base_path, "attack"))
crouch_images = load_images_from_folder(os.path.join(base_path, "crouch"))
slide_images = load_images_from_folder(os.path.join(base_path, "slide"))
dash_images = load_images_from_folder(os.path.join(base_path, "dash"))

# --- VARIABLES ---
attacking = False
attack_frame_index = 0
attack_timer = 0
ATTACK_DURATION = len(attack_images) * ANIMATION_DELAY

player_x = 100
player_y = GROUND_Y - 50
player_velocity_x = 0
player_velocity_y = 0
on_ground = False
crouching = False
facing_right = True

frame_index = 0
animation_counter = 0
current_animation = idle_images
scroll_x = 0

# --- DASH VARIABLES ---
dashing = False
dash_timer = 0
dash_direction = 1
dash_cooldown_timer = 0

# --- PLATEFORMES ---
class Platform:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
    def draw(self, surface, scroll_x):
        pygame.draw.rect(surface, (139, 69, 19), self.rect.move(-scroll_x, 0))

platforms = [
    Platform(0, GROUND_Y, 3000, 50),
    Platform(300, GROUND_Y - 100, 100, 20),
    Platform(500, GROUND_Y - 150, 150, 20),
    Platform(700, GROUND_Y - 180, 100, 20),
    Platform(900, GROUND_Y - 120, 200, 20),
    Platform(1200, GROUND_Y - 180, 120, 20),
    Platform(1350, GROUND_Y - 250, 100, 20),
    Platform(1500, GROUND_Y - 150, 100, 20),
    Platform(1700, GROUND_Y - 100, 200, 20),
    Platform(2000, GROUND_Y - 180, 150, 20),
    Platform(2300, GROUND_Y - 150, 200, 20),
]

# --- BOUCLE PRINCIPALE ---
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

    # --- INPUTS ---
    if keys[pygame.K_LEFT]:
        player_velocity_x = -PLAYER_SPEED
        moving = True
        facing_right = False
    if keys[pygame.K_RIGHT]:
        player_velocity_x = PLAYER_SPEED
        moving = True
        facing_right = True
    if keys[pygame.K_UP] and on_ground:
        player_velocity_y = JUMP_STRENGTH
        on_ground = False
    if keys[pygame.K_a] and not attacking:
        attacking = True
        attack_timer = ATTACK_DURATION
        attack_frame_index = 0
        animation_counter = 0
    crouching = keys[pygame.K_DOWN] and on_ground and not attacking

    # --- DASH D + FLÈCHE ---
    if dash_cooldown_timer > 0:
        dash_cooldown_timer -= 1

    if keys[pygame.K_d] and on_ground and not dashing and dash_cooldown_timer == 0:
        if keys[pygame.K_LEFT]:
            dashing = True
            dash_timer = DASH_DURATION
            dash_direction = -1
            dash_cooldown_timer = DASH_COOLDOWN
        elif keys[pygame.K_RIGHT]:
            dashing = True
            dash_timer = DASH_DURATION
            dash_direction = 1
            dash_cooldown_timer = DASH_COOLDOWN

    if dashing:
        player_velocity_x = dash_direction * DASH_SPEED
        dash_timer -= 1
        if dash_timer <= 0:
            dashing = False

    # --- ANIMATION ---
    previous_animation = current_animation

    if attacking and len(attack_images) > 0:
        attack_timer -= 1
        animation_counter += 1
        if animation_counter >= ANIMATION_DELAY:
            animation_counter = 0
            attack_frame_index = (attack_frame_index + 1) % len(attack_images)
        current_frame = attack_images[attack_frame_index]
        if not facing_right:
            current_frame = pygame.transform.flip(current_frame, True, False)
        if attack_timer <= 0:
            attacking = False
    else:
        if dashing and len(dash_images) > 0:
            current_animation = dash_images
        elif crouching and moving and len(slide_images) > 0:
            current_animation = slide_images
        elif crouching:
            current_animation = crouch_images
        elif not on_ground:
            current_animation = jump_images if player_velocity_y < 0 else fall_images
        else:
            current_animation = run_images if moving else idle_images

        if current_animation is not previous_animation:
            frame_index = 0
            animation_counter = 0

        if len(current_animation) == 0:
            current_frame = pygame.Surface((50, 50))
            current_frame.fill((255, 0, 0))
        else:
            animation_counter += 1
            if animation_counter >= ANIMATION_DELAY:
                animation_counter = 0
                frame_index = (frame_index + 1) % len(current_animation)
            current_frame = current_animation[frame_index]
            if not facing_right:
                current_frame = pygame.transform.flip(current_frame, True, False)

    # --- PHYSIQUE ---
    player_x += player_velocity_x
    player_rect = pygame.Rect(player_x, player_y, 50, 50)

    for platform in platforms:
        if player_rect.colliderect(platform.rect):
            if player_velocity_x > 0:
                player_x = platform.rect.left - 50
            elif player_velocity_x < 0:
                player_x = platform.rect.right
            player_rect.x = player_x

    player_x = max(0, min(player_x, 3000 - 50))
    player_rect.x = player_x

    player_velocity_y += GRAVITY
    player_y += player_velocity_y
    player_rect.y = player_y

    on_ground = False
    for platform in platforms:
        if player_rect.colliderect(platform.rect):
            if player_velocity_y > 0 and player_rect.bottom - player_velocity_y <= platform.rect.top + 10:
                player_y = platform.rect.top - 50
                player_velocity_y = 0
                on_ground = True
                player_rect.y = player_y
            elif player_velocity_y < 0 and player_rect.top - player_velocity_y >= platform.rect.bottom:
                player_y = platform.rect.bottom
                player_velocity_y = 0
                player_rect.y = player_y

    if player_y > HEIGHT + 100:
        player_x = 100
        player_y = GROUND_Y - 50
        player_velocity_y = 0
        player_rect.x = player_x
        player_rect.y = player_y

    # --- SCROLLING ---
    if player_x - scroll_x > WIDTH * 0.6:
        scroll_x = player_x - WIDTH * 0.6
    elif player_x - scroll_x < WIDTH * 0.3:
        scroll_x = player_x - WIDTH * 0.3
    scroll_x = max(0, scroll_x)

    # --- DESSIN ---
    screen.fill(BACKGROUND_COLOR)
    for platform in platforms:
        platform.draw(screen, scroll_x)
    screen.blit(current_frame, (player_x - scroll_x, player_y))
    pygame.display.flip()

pygame.quit()
