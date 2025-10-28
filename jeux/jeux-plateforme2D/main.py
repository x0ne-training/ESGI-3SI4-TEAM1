import pygame
import os
import math

pygame.init()

# --- CONFIGURATION ---
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Daenerys Journey")
clock = pygame.time.Clock()

# --- COULEURS ---
BACKGROUND_COLOR = (135, 206, 235)
GROUND_COLOR = (139, 69, 19)

# --- FOND D'ÉCRAN ---
background_image_path = r"c:\Users\idimi\Documents\Codage\Python\ESGI-3SI4-TEAM1\jeux\jeux-plateforme2D\biome\forest.png"
if os.path.exists(background_image_path):
    background_image = pygame.image.load(background_image_path).convert()
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
else:
    print("❌ Image de fond introuvable, utilisation de la couleur de fond")
    background_image = None

# --- PLAYER ---
PLAYER_SPEED = 5
GRAVITY = 1
JUMP_STRENGTH = -15
ANIMATION_DELAY = 5
DASH_SPEED = 12
DASH_DURATION = 15
DASH_COOLDOWN = 300
DASH_ATTACK_SPEED = 15
DASH_ATTACK_DURATION = 15
DASH_ATTACK_COOLDOWN = 500

GROUND_Y = HEIGHT - 50

# --- ÉTATS DU JEU ---
MENU = 0
OPTIONS = 1
GAME = 2
state = MENU

# --- VARIABLES MENU ---
menu_options = ["Jouer", "Options", "Quitter"]
selected_option = 0
highlight_counter = 0
volume = 0.5
options_list = ["Volume"]
selected_option_options = 0

# --- CHARGEMENT DES IMAGES ---
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

base_path = r"c:\Users\idimi\Documents\Codage\Python\ESGI-3SI4-TEAM1\jeux\jeux-plateforme2D"
idle_images = load_images_from_folder(os.path.join(base_path, "idle"))
run_images = load_images_from_folder(os.path.join(base_path, "run"))
jump_images = load_images_from_folder(os.path.join(base_path, "jump"))
fall_images = load_images_from_folder(os.path.join(base_path, "fall"))
attack_images = load_images_from_folder(os.path.join(base_path, "attack"))
crouch_images = load_images_from_folder(os.path.join(base_path, "crouch"))
slide_images = load_images_from_folder(os.path.join(base_path, "slide"))
dash_images = load_images_from_folder(os.path.join(base_path, "dash"))
dash_attack_images = load_images_from_folder(os.path.join(base_path, "dash_attack"))

# --- VARIABLES JOUEUR ---
player_health = 100
max_health = 100
attacking = False
attack_frame_index = 0
attack_timer = 0

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

# Dash normal
dashing = False
dash_timer = 0
dash_direction = 1
dash_cooldown_timer = 0

# Dash attack
dashing_attack = False
dash_attack_timer = 0
dash_attack_direction = 1
dash_attack_cooldown_timer = 0

ATTACK_DURATION = max(len(attack_images) * ANIMATION_DELAY, 20)

# --- PLATEFORMES ---
class Platform:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
    def draw(self, surface, scroll_x):
        pygame.draw.rect(surface, GROUND_COLOR, self.rect.move(-scroll_x, 0))

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

# --- FONCTIONS MENU ---
def draw_menu(screen):
    global highlight_counter
    screen.fill((30, 30, 40))
    font_title = pygame.font.Font(None, 80)
    title = font_title.render("DAENERYS JOURNEY", True, (255, 255, 255))
    screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//6))

    font_option = pygame.font.Font(None, 50)
    highlight_color = (255, 255, 0)
    base_color = (200, 200, 200)

    highlight_intensity = (1 + 0.5 * math.sin(highlight_counter / 10))
    highlight_counter += 1

    for i, option in enumerate(menu_options):
        color = highlight_color if i == selected_option else base_color
        if i == selected_option:
            color = (min(255, int(color[0]*highlight_intensity)),
                    min(255, int(color[1]*highlight_intensity)),
                    0)
        text = font_option.render(option, True, color)
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 + i*70))

    pygame.display.flip()

def draw_options(screen):
    screen.fill((20, 20, 50))
    font_title = pygame.font.Font(None, 70)
    title = font_title.render("OPTIONS", True, (255, 255, 255))
    screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//6))

    font_text = pygame.font.Font(None, 50)
    for i, opt in enumerate(options_list):
        color = (255, 255, 0) if i == selected_option_options else (200, 200, 200)
        value_text = f"{int(volume*100)}%" if opt == "Volume" else ""
        text = font_text.render(f"{opt}: {value_text}", True, color)
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 + i*70))

    info_text = font_text.render("Appuyez sur ESC pour revenir", True, (180, 180, 180))
    screen.blit(info_text, (WIDTH//2 - info_text.get_width()//2, HEIGHT - 100))
    pygame.display.flip()

# --- BOUCLE PRINCIPALE ---
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # --- MENU ---
    if state == MENU:
        draw_menu(screen)
        if keys[pygame.K_DOWN]:
            selected_option = (selected_option + 1) % len(menu_options)
            pygame.time.wait(150)
        elif keys[pygame.K_UP]:
            selected_option = (selected_option - 1) % len(menu_options)
            pygame.time.wait(150)
        elif keys[pygame.K_RETURN]:
            if menu_options[selected_option] == "Jouer":
                state = GAME
            elif menu_options[selected_option] == "Options":
                state = OPTIONS
            elif menu_options[selected_option] == "Quitter":
                running = False
        continue

    # --- OPTIONS ---
    if state == OPTIONS:
        draw_options(screen)
        if keys[pygame.K_DOWN]:
            selected_option_options = (selected_option_options + 1) % len(options_list)
            pygame.time.wait(150)
        elif keys[pygame.K_UP]:
            selected_option_options = (selected_option_options - 1) % len(options_list)
            pygame.time.wait(150)
        elif keys[pygame.K_RIGHT]:
            if options_list[selected_option_options] == "Volume":
                volume = min(1.0, volume + 0.05)
                pygame.time.wait(100)
        elif keys[pygame.K_LEFT]:
            if options_list[selected_option_options] == "Volume":
                volume = max(0.0, volume - 0.05)
                pygame.time.wait(100)
        elif keys[pygame.K_ESCAPE]:
            state = MENU
        continue

    # --- JEU ---
    moving = False
    player_velocity_x = 0

    # Déplacements
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

    # Attaque normale
    if keys[pygame.K_a] and not attacking and not dashing and not dashing_attack:
        attacking = True
        attack_timer = ATTACK_DURATION
        attack_frame_index = 0
        animation_counter = 0

    crouching = keys[pygame.K_DOWN] and on_ground and not attacking

    # Cooldowns
    if dash_attack_cooldown_timer > 0: dash_attack_cooldown_timer -= 1
    if dash_cooldown_timer > 0: dash_cooldown_timer -= 1

    # Dash attack
    if keys[pygame.K_z] and on_ground and not dashing_attack and dash_attack_cooldown_timer == 0:
        attacking = False
        if keys[pygame.K_LEFT]:
            dashing_attack = True
            dash_attack_timer = DASH_ATTACK_DURATION
            dash_attack_direction = -1
            dash_attack_cooldown_timer = DASH_ATTACK_COOLDOWN
        elif keys[pygame.K_RIGHT]:
            dashing_attack = True
            dash_attack_timer = DASH_ATTACK_DURATION
            dash_attack_direction = 1
            dash_attack_cooldown_timer = DASH_ATTACK_COOLDOWN

    # Dash normal
    if keys[pygame.K_d] and on_ground and not dashing and not dashing_attack and dash_cooldown_timer == 0:
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

    # --- ANIMATIONS ---
    previous_animation = current_animation

    if dashing_attack:
        current_animation = dash_attack_images
        if len(current_animation) == 0:
            current_frame = pygame.Surface((50, 50))
            current_frame.fill((255, 128, 0))
        else:
            animation_counter += 1
            if animation_counter >= ANIMATION_DELAY:
                animation_counter = 0
                frame_index = (frame_index + 1) % len(current_animation)
            current_frame = current_animation[frame_index]
        if not facing_right:
            current_frame = pygame.transform.flip(current_frame, True, False)

    elif attacking:
        current_animation = attack_images
        if len(current_animation) == 0:
            current_frame = pygame.Surface((50, 50))
            current_frame.fill((255, 0, 0))
        else:
            attack_timer -= 1
            animation_counter += 1
            if animation_counter >= ANIMATION_DELAY:
                animation_counter = 0
                attack_frame_index = (attack_frame_index + 1) % len(current_animation)
            current_frame = current_animation[attack_frame_index]
        if not facing_right:
            current_frame = pygame.transform.flip(current_frame, True, False)
        if attack_timer <= 0:
            attacking = False
            attack_frame_index = 0

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

    # --- DESSIN DU FOND DÉFILANT ---
    if background_image:
        rel_x = -scroll_x % background_image.get_width()
        screen.blit(background_image, (rel_x - background_image.get_width(), 0))
        if rel_x < WIDTH:
            screen.blit(background_image, (rel_x, 0))
    else:
        screen.fill(BACKGROUND_COLOR)

    # --- DESSIN DES PLATEFORMES ET JOUEUR ---
    for platform in platforms:
        platform.draw(screen, scroll_x)
    screen.blit(current_frame, (player_x - scroll_x, player_y))

    # --- BARRES ---
    bar_width = 50
    bar_height = 5
    bar_x = player_x - scroll_x
    bar_y = player_y - 10

    max_cooldown = max(DASH_COOLDOWN, DASH_ATTACK_COOLDOWN)
    current_cooldown = max(dash_cooldown_timer, dash_attack_cooldown_timer)
    ratio = current_cooldown / max_cooldown
    pygame.draw.rect(screen, (0, 0, 0), (bar_x, bar_y, bar_width, bar_height))
    pygame.draw.rect(screen, (0, 0, 255), (bar_x, bar_y, bar_width * ratio, bar_height))

    # Barre de vie
    health_ratio = player_health / max_health
    pygame.draw.rect(screen, (0, 0, 0), (bar_x, bar_y - 10, bar_width, bar_height))
    pygame.draw.rect(screen, (0, 255, 0), (bar_x, bar_y - 10, bar_width * health_ratio, bar_height))

    pygame.display.flip()

pygame.quit()
