import pygame
import os
import json
import math

pygame.init()

# --- CONFIGURATION ---
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Daenerys Journey")
clock = pygame.time.Clock()

# --- COULEURS ---
GROUND_COLOR = (139, 69, 19)
BACKGROUND_COLOR = (135, 206, 235)

# --- ETATS DU JEU ---
MENU = 0
OPTIONS = 1
LEVEL_SELECT = 2
GAME = 3
state = MENU

# --- VARIABLES MENU ---
menu_options = ["Jouer", "Options", "Quitter"]
selected_option = 0
highlight_counter = 0

# --- VARIABLES OPTIONS ---
volume = 0.5

# --- VARIABLES SELECTION DE NIVEAU ---
selected_level = 0
level_files = ["level1.json", "level2.json", "level3.json", "level4.json", "level5.json", "level6.json", "level7.json", "level8.json", "level9.json", "level10.json", "level11.json", "level12.json",]  # fichiers JSON des niveaux
levels_per_page = 10
current_page = 0
total_pages = (len(level_files) - 1) // levels_per_page + 1

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

player_health = 100
max_health = 100
attacking = False
attack_timer = 0
player_x = 100
player_y = 100
player_velocity_x = 0
player_velocity_y = 0
on_ground = False
crouching = False
facing_right = True
moving = False

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

# --- CHARGEMENT DES IMAGES ---
def load_images_from_folder(folder, size=(50,50)):
    if not os.path.exists(folder):
        # print pour debug, pas d'erreur levée pour garder le jeu lançable
        print(f"❌ Dossier introuvable : {folder}")
        return []
    images=[]
    for filename in sorted(os.listdir(folder)):
        if filename.endswith(".png"):
            path=os.path.join(folder,filename)
            try:
                img=pygame.image.load(path).convert_alpha()
                img=pygame.transform.scale(img,size)
                images.append(img)
            except Exception as e:
                print(f"⚠️ Erreur chargement {filename}: {e}")
    return images

# Remplace par ton chemin de base
base_path = r"c:\Users\idimi\Documents\Codage\Python\ESGI-3SI4-TEAM1\jeux\jeux-plateforme2D\assets"

# Player animations (tu en avais déjà)
player_base = os.path.join(base_path,"player")
idle_images=load_images_from_folder(os.path.join(player_base,"idle"))
run_images=load_images_from_folder(os.path.join(player_base,"run"))
jump_images=load_images_from_folder(os.path.join(player_base,"jump"))
fall_images=load_images_from_folder(os.path.join(player_base,"fall"))
attack_images=load_images_from_folder(os.path.join(player_base,"attack"))
crouch_images=load_images_from_folder(os.path.join(player_base,"crouch"))
slide_images=load_images_from_folder(os.path.join(player_base,"slide"))
dash_images=load_images_from_folder(os.path.join(player_base,"dash"))
dash_attack_images=load_images_from_folder(os.path.join(player_base,"dash_attack"))

# --- ENEMY (WOLF) ANIMATIONS ---
# On suppose un dossier "wolf" à la racine base_path contenant des sous-dossiers "idle","walk","attack","death"
enemy_base = os.path.join(base_path, "enemies")
wolf_base = os.path.join(enemy_base, "wolf")
wolf_idle_images = load_images_from_folder(os.path.join(wolf_base, "idle"), size=(40,50))
wolf_walk_images = load_images_from_folder(os.path.join(wolf_base, "walk"), size=(40,50))
wolf_attack_images = load_images_from_folder(os.path.join(wolf_base, "attack"), size=(50,50))
wolf_death_images = load_images_from_folder(os.path.join(wolf_base, "death"), size=(50,50))

# --- FOND MENU ---
biome_base = os.path.join(base_path,r"levels\biome")
menu_background_path = os.path.join(biome_base,"forest.png")
if os.path.exists(menu_background_path):
    menu_background=pygame.image.load(menu_background_path).convert()
    menu_background=pygame.transform.scale(menu_background,(WIDTH,HEIGHT))
else:
    menu_background=None

# --- ANIMATION IDLE MENU ---
menu_idle_index=0
menu_idle_counter=0
menu_idle_speed=5

# --- CLASSES ---
class Platform:
    def __init__(self,x,y,width,height):
        self.rect=pygame.Rect(x,y,width,height)
    def draw(self,surface,scroll_x):
        pygame.draw.rect(surface,GROUND_COLOR,self.rect.move(-scroll_x,0))

class Barrier:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
    def draw(self, surface, scroll_x):
        # invisible
        pass

# --- CLASSE ENNEMI AVEC SPRITES ---

ENEMY_STATS = {
    "wolf": {
        "health": 100,
        "speed": 2,
        "patrol_range": 100,
        "attack_damage": 10,
        "attack_range": 60,
        "size":(40,50)
    },
    "bear": {
        "health": 300,
        "speed": 1,
        "patrol_range": 50,
        "attack_damage": 20,
        "attack_range": 60,
        "size":(70,70)
    }
}

class Enemy:
    def __init__(self, x, y, enemy_type="wolf"):
        # --- Statistiques de base ---
        stats = ENEMY_STATS.get(enemy_type, ENEMY_STATS["wolf"])
        self.type = enemy_type
        self.health = stats["health"]
        self.max_health = stats["health"]
        self.speed = stats["speed"]
        self.patrol_range = stats["patrol_range"]
        self.attack_damage = stats.get("attack_damage", 10)
        self.attack_range = stats.get("attack_range", 60)
        self.size = stats["size"]

        # --- Position et état ---
        self.x = x
        self.start_x = x
        self.ground_y = y
        self.direction = 1
        self.state = "idle"
        self.alive = True
        self.dying = False
        self.dead = False

        # --- Animation ---
        self.animations = {}
        enemy_base_path = os.path.join(base_path, "enemies", self.type)

        def safe_load_images(folder_name, size=self.size):
            path = os.path.join(enemy_base_path, folder_name)
            images = []
            if os.path.exists(path):
                for img_file in sorted(os.listdir(path)):
                    if img_file.endswith(".png"):
                        try:
                            img = pygame.image.load(os.path.join(path, img_file)).convert_alpha()
                            img = pygame.transform.scale(img, size)
                            images.append(img)
                        except Exception as e:
                            print(f"⚠️ Erreur chargement {img_file}: {e}")
            if not images:
                # Fallback carré rouge
                surf = pygame.Surface(size, pygame.SRCALPHA)
                surf.fill((255, 0, 0))
                images.append(surf)
            print(f"{self.type} {folder_name}: {len(images)} images chargées")
            return images

        self.animations["idle"] = safe_load_images("idle")
        self.animations["walk"] = safe_load_images("walk")
        self.animations["attack"] = safe_load_images("attack")
        self.animations["death"] = safe_load_images("death")

        # --- Contrôle animation ---
        self.frame_index = 0
        self.animation_counter = 0
        self.image = self.animations["idle"][0]
        self.rect = self.image.get_rect(midbottom=(x, self.ground_y))

        # --- Combat ---
        self.attacking = False
        self.attack_cooldown = 0
        self.attack_cooldown_max = 90
        self.has_hit_player = False
        self.hit_flash_timer = 0
        self.ready_to_hit = False

    def update(self, player_rect):
        if self.dead:
            return

        # --- Effet visuel hit ---
        if self.hit_flash_timer > 0:
            self.hit_flash_timer -= 1

        # --- Mort / dying ---
        if self.dying:
            frames = self.animations.get("death", [])
            if frames:
                self.animation_counter += 1
                if self.animation_counter > 10:
                    self.animation_counter = 0
                    self.frame_index += 1
                    if self.frame_index >= len(frames):
                        self.dead = True
                        self.alive = False
                        self.frame_index = len(frames) - 1
            return

        # --- Distance joueur ---
        distance_x = abs(player_rect.centerx - self.rect.centerx)

        # --- Gestion cooldown ---
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        # --- Si en attaque ---
        if self.attacking:
            frames = self.animations.get("attack", [])
            if frames:
                self.animation_counter += 1
                if self.animation_counter > 10:
                    self.animation_counter = 0
                    self.frame_index += 1

                    # --- Déclenchement du coup sur UNE frame ---
                    if self.frame_index == len(frames) // 2:
                        self.ready_to_hit = True  # l’attaque frappe à cette frame

                    # --- Fin d'attaque ---
                    if self.frame_index >= len(frames):
                        self.attacking = False
                        self.attack_cooldown = self.attack_cooldown_max
                        self.state = "idle"
                        self.frame_index = 0
                        self.animation_counter = 0
                        self.has_hit_player = False
                        self.ready_to_hit = False

        # --- Déclenche attaque ---
        elif distance_x < self.attack_range and self.attack_cooldown == 0:
            self.attacking = True
            self.state = "attack"
            self.frame_index = 0
            self.animation_counter = 0
            self.has_hit_player = False
            self.ready_to_hit = False

        # --- Sinon, patrouille ---
        else:
            self.state = "walk"
            self.x += self.direction * self.speed
            if abs(self.x - self.start_x) > self.patrol_range:
                self.direction *= -1

        # --- Mise à jour du rect ---
        self.rect.x = int(self.x)
        self.rect.bottom = self.ground_y

        # --- Animation idle / walk ---
        if self.state in ["idle", "walk"]:
            frames = self.animations.get(self.state, [])
            if frames:
                self.animation_counter += 1
                if self.animation_counter > 10:
                    self.animation_counter = 0
                    self.frame_index = (self.frame_index + 1) % len(frames)

    def draw(self, surface, scroll_x):
        if self.dead:
            return

        frames = self.animations.get(self.state, [])
        if not frames:
            frames = [pygame.Surface(self.size)]
        self.frame_index %= len(frames)
        self.image = frames[self.frame_index]

        img = self.image
        if self.direction < 0:
            img = pygame.transform.flip(img, True, False)

        # --- Flash rouge lors du hit ---
        if self.hit_flash_timer > 0:
            flash = img.copy()
            flash.fill((255, 0, 0, 100), special_flags=pygame.BLEND_RGBA_ADD)
            img = flash

        surface.blit(img, (self.rect.x - scroll_x, self.rect.y))

        # --- Barre de vie ---
        bar_width = 50
        bar_height = 5
        bar_x = self.rect.x - scroll_x + (self.rect.width - bar_width)//2
        bar_y = self.rect.y - 10
        pygame.draw.rect(surface, (0, 0, 0), (bar_x, bar_y, bar_width, bar_height))
        pygame.draw.rect(surface, (255, 0, 0),
                         (bar_x, bar_y, bar_width * (self.health / self.max_health), bar_height))

    def take_damage(self, dmg):
        if self.dead or self.dying:
            return
        self.health -= dmg
        self.hit_flash_timer = 15
        if self.health <= 0:
            self.dying = True
            self.frame_index = 0
            self.animation_counter = 0
            self.state = "death"

    def attack_player(self, player_rect, player_health):
        # Attaque uniquement si l’ennemi est dans la frame de frappe
        if not self.attacking or self.dead or self.dying:
            return player_health

        if self.ready_to_hit and not self.has_hit_player and self.rect.colliderect(player_rect):
            player_health -= self.attack_damage
            player_health = max(player_health, 0)
            self.has_hit_player = True
            self.ready_to_hit = False  # le coup est consommé

        return player_health

# --- FONCTIONS MENU ---
def draw_menu(screen):
    global highlight_counter, menu_idle_index, menu_idle_counter
    if menu_background:
        screen.blit(menu_background,(0,0))
    else:
        screen.fill((30,30,40))
    # idle personnage agrandi
    if len(idle_images)>0:
        menu_idle_counter+=1
        if menu_idle_counter>=menu_idle_speed:
            menu_idle_counter=0
            menu_idle_index=(menu_idle_index+1)%len(idle_images)
        idle_frame=idle_images[menu_idle_index]
        scale_factor=3
        idle_frame_large=pygame.transform.scale(idle_frame,(idle_frame.get_width()*scale_factor,idle_frame.get_height()*scale_factor))
        screen.blit(idle_frame_large,(50,HEIGHT//2-idle_frame_large.get_height()//2))
    font_title=pygame.font.Font(None,80)
    title=font_title.render("DAENERYS JOURNEY",True,(255,255,255))
    screen.blit(title,(WIDTH//2-title.get_width()//2,HEIGHT//6))
    font_option=pygame.font.Font(None,50)
    highlight_color=(255,255,0)
    base_color=(200,200,200)
    highlight_intensity=(1 + 0.5*math.sin(highlight_counter/10))
    highlight_counter+=1
    for i,option in enumerate(menu_options):
        color=highlight_color if i==selected_option else base_color
        if i==selected_option:
            color=(min(255,int(color[0]*highlight_intensity)),min(255,int(color[1]*highlight_intensity)),0)
        text=font_option.render(option,True,color)
        screen.blit(text,(WIDTH//2-text.get_width()//2,HEIGHT//2+i*70))
    pygame.display.flip()

# --- SELECTION DE NIVEAU ---
def draw_level_select(screen):
    screen.fill((50,50,80))
    font=pygame.font.Font(None,40)
    circle_radius=40
    spacing_x=120
    spacing_y=120
    start_x=WIDTH//2-(5*spacing_x)//2+spacing_x//2
    start_y=HEIGHT//3
    start_index = current_page * levels_per_page
    end_index = min(start_index + levels_per_page, len(level_files))
    page_levels = range(start_index, end_index)
    
    screen.fill((50,50,80))
    font = pygame.font.Font(None,40)
    circle_radius = 40
    spacing_x = 120
    spacing_y = 120
    start_x = WIDTH//2-(5*spacing_x)//2+spacing_x//2
    start_y = HEIGHT//3
    
    for idx, i in enumerate(page_levels):
        row = idx // 5
        col = idx % 5
        x = start_x + col * spacing_x
        y = start_y + row * spacing_y
        color = (200,200,200) if i != selected_level else (255,255,0)
        pygame.draw.circle(screen,color,(x,y),circle_radius)
        pygame.draw.circle(screen,(0,0,0),(x,y),circle_radius,3)
        text = font.render(str(i+1), True, (0,0,0))
        screen.blit(text,(x-text.get_width()//2,y-text.get_height()//2))
    
    # Info + boutons page
    font_small = pygame.font.Font(None,30)
    info = font_small.render("Flèches : sélectionner, Entrée : jouer",True,(200,200,200))
    screen.blit(info,(WIDTH//2-info.get_width()//2,HEIGHT-50))
    
    # Boutons page
    page_info = font_small.render(f"Page {current_page+1}/{total_pages}", True, (255,255,255))
    screen.blit(page_info, (WIDTH//2-page_info.get_width()//2, HEIGHT-80))
    
    pygame.display.flip()

def handle_level_select_event(event):
    global selected_level, state, player_x, player_y, platforms, barriers, scroll_x, background_image, level_data, enemies
    global current_page, levels_per_page

    if event.key == pygame.K_LEFT:
        if selected_level % 5 == 0 and selected_level > current_page*levels_per_page:
            selected_level -= 1
        elif selected_level % 5 != 0:
            selected_level -= 1
    elif event.key == pygame.K_RIGHT:
        if selected_level % 5 == 4 and selected_level < (current_page+1)*levels_per_page-1 and selected_level < len(level_files)-1:
            selected_level += 1
        elif selected_level % 5 != 4:
            selected_level += 1

    elif event.key == pygame.K_UP:
        if selected_level >= 5:
            selected_level -= 5
    elif event.key == pygame.K_DOWN:
        if selected_level < 5:
            selected_level += 5

    if event.key == pygame.K_PAGEUP:
        current_page = (current_page - 1) % total_pages
        selected_level = current_page * levels_per_page
    elif event.key == pygame.K_PAGEDOWN:
        current_page = (current_page + 1) % total_pages
        selected_level = current_page * levels_per_page
    elif event.key == pygame.K_RETURN:
        # ... reste inchangé

        # --- Charger le niveau ---
        level_data = load_level_json(level_files[selected_level])
        if level_data:
            player_x,player_y = level_data["player_start"]
            platforms = [Platform(p["x"],p["y"],p["width"],p["height"]) for p in level_data["platforms"]]
            barriers = []
            if "barriers" in level_data:
                for b in level_data["barriers"]:
                    barriers.append(Barrier(b["x"], b["y"], b["width"], b["height"]))
            # Charger les ennemis depuis JSON
            enemies = []
            if "enemies" in level_data:
                for e in level_data["enemies"]:
                    enemy_type = e.get("type", "wolf")  # type par défaut
                    enemies.append(Enemy(e["x"], e["y"], enemy_type))

            else:
                enemies = []

            # Charger le fond du biome
            biome_path = os.path.join(base_path, r"levels\biome", level_data["biome"])
            if os.path.exists(biome_path):
                background_image = pygame.image.load(biome_path).convert_alpha()
                background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
            else:
                print(f"❌ Biome introuvable : {biome_path}")
                background_image = None
            scroll_x=0
            state=GAME
        else:
            print(f"❌ Impossible de charger le niveau {selected_level+1}.")

# --- CHARGEMENT NIVEAU JSON ---
def load_level_json(filename):
    path = os.path.join(base_path,"levels",filename)
    if not os.path.exists(path):
        print(f"❌ Niveau {filename} introuvable !")
        return None
    with open(path,"r") as f:
        data=json.load(f)
    # Vérifier les clés minimales
    if "player_start" not in data or "platforms" not in data or "biome" not in data:
        print(f"❌ Niveau {filename} invalide !")
        return None
    return data

# --- GESTION ANIMATIONS (PLAYER) ---
frame_indices = {name:0 for name in ["idle","run","jump","fall","attack","dash","dash_attack","crouch","slide"]}
animation_counters = {name:0 for name in ["idle","run","jump","fall","attack","dash","dash_attack","crouch","slide"]}

def frame_index_animation(anim_list, name):
    if len(anim_list)==0: return 0
    animation_counters[name]+=1
    if animation_counters[name]>=ANIMATION_DELAY:
        animation_counters[name]=0
        frame_indices[name]=(frame_indices[name]+1)%len(anim_list)
    return frame_indices[name]

def dash_attack_timer_step():
    global dashing_attack, dash_attack_timer
    dash_attack_timer-=1
    frame_index_animation(dash_attack_images, "dash_attack")
    if dash_attack_timer<=0:
        dashing_attack=False
        frame_indices["dash_attack"]=0
        animation_counters["dash_attack"]=0

def dash_timer_step():
    global dashing, dash_timer
    dash_timer-=1
    frame_index_animation(dash_images, "dash")
    if dash_timer<=0:
        dashing=False
        frame_indices["dash"]=0
        animation_counters["dash"]=0

def attack_timer_step():
    global attacking, attack_timer
    attack_timer-=1
    frame_index_animation(attack_images, "attack")
    if attack_timer<=0:
        attacking=False
        frame_indices["attack"]=0
        animation_counters["attack"]=0

def get_current_frame():
    global moving
    if dashing_attack and len(dash_attack_images)>0:
        dash_attack_timer_step()
        current_animation=dash_attack_images
        index=frame_indices["dash_attack"]
    elif dashing and len(dash_images)>0:
        dash_timer_step()
        current_animation=dash_images
        index=frame_indices["dash"]
    elif attacking and len(attack_images)>0:
        attack_timer_step()
        current_animation=attack_images
        index=frame_indices["attack"]
    else:
        if crouching and moving and len(slide_images)>0:
            current_animation=slide_images
            index=frame_index_animation(slide_images,"slide")
        elif crouching and len(crouch_images)>0:
            current_animation=crouch_images
            index=frame_index_animation(crouch_images,"crouch")
        elif not on_ground:
            if player_velocity_y<0 and len(jump_images)>0:
                current_animation=jump_images
                index=frame_index_animation(jump_images,"jump")
            elif player_velocity_y>=0 and len(fall_images)>0:
                current_animation=fall_images
                index=frame_index_animation(fall_images,"fall")
            else:
                current_animation=idle_images
                index=frame_index_animation(idle_images,"idle")
        elif moving and len(run_images)>0:
            current_animation=run_images
            index=frame_index_animation(run_images,"run")
        else:
            current_animation=idle_images
            index=frame_index_animation(idle_images,"idle")

    if len(current_animation)==0:
        frame=pygame.Surface((50,50))
        frame.fill((255,0,0))
    else:
        index=min(index,len(current_animation)-1)
        frame=current_animation[index]

    if not facing_right:
        frame=pygame.transform.flip(frame,True,False)
    return frame

# --- BOUCLE PRINCIPALE ---
# --- Variables pour gérer les dégâts par attaque ---
player_has_hit_normal = False
player_has_hit_dash = False

# --- BOUCLE PRINCIPALE ---
running = True
scroll_x = 0
platforms = []
barriers = []
enemies = []
background_image = None
level_data = None

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if state == MENU:
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if menu_options[selected_option] == "Jouer":
                        state = LEVEL_SELECT
                    elif menu_options[selected_option] == "Options":
                        state = OPTIONS
                    elif menu_options[selected_option] == "Quitter":
                        running = False
            elif state == LEVEL_SELECT:
                handle_level_select_event(event)
            elif state == OPTIONS:
                if event.key == pygame.K_ESCAPE:
                    state = MENU

    keys = pygame.key.get_pressed()

    # --- ETATS ---
    if state == MENU:
        draw_menu(screen)
        continue
    elif state == LEVEL_SELECT:
        draw_level_select(screen)
        continue
    elif state == OPTIONS:
        screen.fill((20, 20, 50))
        pygame.display.flip()
        continue
    elif state == GAME:
        moving = False
        player_velocity_x = 0

        # --- MOUVEMENT ---
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

        # --- Cooldowns ---
        if dash_attack_cooldown_timer > 0:
            dash_attack_cooldown_timer -= 1
        if dash_cooldown_timer > 0:
            dash_cooldown_timer -= 1

        # --- Attaque normale ---
        if keys[pygame.K_a] and on_ground and not dashing_attack and not dashing:
            attacking = True
            attack_timer = len(attack_images) * ANIMATION_DELAY if len(attack_images) > 0 else ANIMATION_DELAY*4
            frame_indices["attack"] = 0
            animation_counters["attack"] = 0
            player_has_hit_normal = False  # reset dégâts pour cette attaque

        # --- Dash attack ---
        if keys[pygame.K_z] and on_ground and not dashing_attack and dash_attack_cooldown_timer == 0:
            if keys[pygame.K_LEFT]:
                attacking = False
                player_has_hit_normal = False
                dashing_attack = True
                dash_attack_timer = DASH_ATTACK_DURATION
                dash_attack_direction = -1
                dash_attack_cooldown_timer = DASH_ATTACK_COOLDOWN
                player_has_hit_dash = False
            elif keys[pygame.K_RIGHT]:
                attacking = False
                player_has_hit_normal = False
                dashing_attack = True
                dash_attack_timer = DASH_ATTACK_DURATION
                dash_attack_direction = 1
                dash_attack_cooldown_timer = DASH_ATTACK_COOLDOWN
                player_has_hit_dash = False

        # --- Dash normal ---
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

        crouching = keys[pygame.K_DOWN] and on_ground

        # --- Physique ---
        if dashing_attack:
            player_velocity_x = dash_attack_direction * DASH_ATTACK_SPEED
        elif dashing:
            player_velocity_x = dash_direction * DASH_SPEED

        player_x += player_velocity_x
        player_rect = pygame.Rect(player_x, player_y, 50, 50)

        # --- Collision plateformes et barrières (horizontal) ---
        for obj in platforms + barriers:
            if player_rect.colliderect(obj.rect):
                if player_velocity_x > 0:
                    player_x = obj.rect.left - 50
                elif player_velocity_x < 0:
                    player_x = obj.rect.right
                player_rect.x = player_x

        player_velocity_y += GRAVITY
        player_y += player_velocity_y
        player_rect.y = player_y
        on_ground = False

        # --- Collision plateformes et barrières (vertical) ---
        for obj in platforms + barriers:
            if player_rect.colliderect(obj.rect):
                if player_velocity_y > 0 and player_rect.bottom - player_velocity_y <= obj.rect.top + 10:
                    player_y = obj.rect.top - 50
                    player_velocity_y = 0
                    on_ground = True
                    player_rect.y = player_y
                elif player_velocity_y < 0 and player_rect.top - player_velocity_y >= obj.rect.bottom:
                    player_y = obj.rect.bottom
                    player_velocity_y = 0
                    player_rect.y = player_y

        # --- Reset position si tombe ---
        if level_data and player_y > HEIGHT + 100:
            player_x, player_y = level_data["player_start"]
            player_velocity_y = 0
            player_rect.x = player_x
            player_rect.y = player_y

        # --- Scroll ---
        if player_x - scroll_x > WIDTH * 0.6:
            scroll_x = player_x - WIDTH * 0.6
        elif player_x - scroll_x < WIDTH * 0.3:
            scroll_x = player_x - WIDTH * 0.3
        scroll_x = max(0, scroll_x)

        # --- Dessin fond ---
        if background_image:
            bg_width = background_image.get_width()
            x_offset = -scroll_x % bg_width
            screen.blit(background_image, (x_offset - bg_width, 0))
            screen.blit(background_image, (x_offset, 0))
        else:
            screen.fill(BACKGROUND_COLOR)

        for plat in platforms:
            plat.draw(screen, scroll_x)

        # --- Mise à jour ennemis ---
        alive_enemies = []
        for enemy in enemies:
            enemy.update(player_rect)
            player_health = enemy.attack_player(player_rect, player_health)  # dégâts appliqués ici
            if enemy.dying:
                enemy.frame_index += 1
                if enemy.frame_index >= len(enemy.animations["death"]):
                    enemy.dead = True
                    enemy.alive = False
            if enemy.alive or enemy.dying:
                alive_enemies.append(enemy)
        enemies = alive_enemies

        # --- Dessin ennemis ---
        for enemy in enemies:
            enemy.draw(screen, scroll_x)

        # --- Attaque joueur sur ennemis ---
        if attacking:
            attack_frame_hit = len(attack_images) // 2
            if frame_indices["attack"] == attack_frame_hit and not player_has_hit_normal:
                attack_range = 60
                attack_rect = pygame.Rect(player_x + (25 if facing_right else -attack_range), player_y, attack_range, 50)
                for enemy in enemies:
                    if enemy.alive and not enemy.dying and attack_rect.colliderect(enemy.rect):
                        enemy.take_damage(50)
                player_has_hit_normal = True

        if dashing_attack and not player_has_hit_dash:
            dash_attack_rect = pygame.Rect(player_x + (25 if dash_attack_direction > 0 else -50), player_y, 50, 50)
            for enemy in enemies:
                if enemy.alive and not enemy.dying and dash_attack_rect.colliderect(enemy.rect):
                    enemy.take_damage(100)
            player_has_hit_dash = True

        # --- Dessin joueur ---
        current_frame = get_current_frame()
        screen.blit(current_frame, (player_x - scroll_x, player_y))

        # --- Barres ---
        bar_width = 50
        bar_height = 5
        bar_x = player_x - scroll_x
        bar_y = player_y - 10
        max_cooldown = max(DASH_COOLDOWN, DASH_ATTACK_COOLDOWN)
        current_cooldown = max(dash_cooldown_timer, dash_attack_cooldown_timer)
        ratio = current_cooldown / max_cooldown if max_cooldown > 0 else 0
        pygame.draw.rect(screen, (0, 0, 0), (bar_x, bar_y, bar_width, bar_height))
        pygame.draw.rect(screen, (0, 0, 255), (bar_x, bar_y, bar_width * ratio, bar_height))
        health_ratio = player_health / max_health if max_health > 0 else 0
        pygame.draw.rect(screen, (0, 0, 0), (bar_x, bar_y - 10, bar_width, bar_height))
        pygame.draw.rect(screen, (0, 255, 0), (bar_x, bar_y - 10, bar_width * health_ratio, bar_height))

        pygame.display.flip()

pygame.quit()
