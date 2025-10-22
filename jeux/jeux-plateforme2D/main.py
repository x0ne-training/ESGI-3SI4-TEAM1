import pygame
import os

pygame.init()

# Fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu animé - Mario Style")

# Couleurs
background_color = (135, 206, 235)
ground_color = (0, 255, 0)

# Sol
GROUND_Y = HEIGHT - 50

# Joueur
PLAYER_SPEED = 5
GRAVITY = 1
JUMP_STRENGTH = -15
ANIMATION_DELAY = 5  # frames entre chaque image

# Fonction sécurisée pour charger les images
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
                image = pygame.transform.scale(image, (50, 50))  # redimensionne
                images.append(image)
            except Exception as e:
                print(f"⚠️ Erreur lors du chargement de {filename} : {e}")
    return images

# Chargement des animations
idle_images = load_images_from_folder(r"c:\Users\idimi\Documents\Codage\Python\ESGI-3SI4-TEAM1\jeux\jeux-plateforme2D\idle")
run_images = load_images_from_folder(r"c:\Users\idimi\Documents\Codage\Python\ESGI-3SI4-TEAM1\jeux\jeux-plateforme2D\run")
jump_images = load_images_from_folder(r"c:\Users\idimi\Documents\Codage\Python\ESGI-3SI4-TEAM1\jeux\jeux-plateforme2D\jump")
fall_images = load_images_from_folder(r"c:\Users\idimi\Documents\Codage\Python\ESGI-3SI4-TEAM1\jeux\jeux-plateforme2D\fall")

print(f"✅ {len(idle_images)} images d'idle chargées")
print(f"✅ {len(run_images)} images de run chargées")
print(f"✅ {len(jump_images)} images de jump chargées")
print(f"✅ {len(fall_images)} images de fall chargées")

# Position du joueur
player_x = 100
player_y = GROUND_Y - 50
player_velocity_x = 0
player_velocity_y = 0
on_ground = True

# Animation
frame_index = 0
animation_counter = 0
current_animation = idle_images
facing_right = True

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Entrées clavier
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

    # Gravité
    player_velocity_y += GRAVITY
    player_x += player_velocity_x
    player_y += player_velocity_y

    # Collision avec le sol
    if player_y + 50 >= GROUND_Y:
        player_y = GROUND_Y - 50
        player_velocity_y = 0
        on_ground = True

    if not on_ground:
        if player_velocity_y < 0:
            current_animation = jump_images
        else:
            current_animation = fall_images
    else:
        current_animation = run_images if moving else idle_images

# Vérification et animation
    if len(current_animation) == 0:
        print("⚠️ Aucune image dans current_animation !")
        current_frame = pygame.Surface((50, 50))
        current_frame.fill((255, 0, 0))  # carré rouge de secours
    else:
        animation_counter += 1
        if animation_counter >= ANIMATION_DELAY:
            animation_counter = 0
            frame_index = (frame_index + 1) % len(current_animation)

    frame_index %= len(current_animation)
    current_frame = current_animation[frame_index]

    if not facing_right:
        current_frame = pygame.transform.flip(current_frame, True, False)


    # Affichage
    screen.fill(background_color)
    pygame.draw.rect(screen, ground_color, (0, GROUND_Y, WIDTH, 50))  # Sol
    screen.blit(current_frame, (player_x, player_y))  # Personnage
    pygame.display.flip()

pygame.quit()
