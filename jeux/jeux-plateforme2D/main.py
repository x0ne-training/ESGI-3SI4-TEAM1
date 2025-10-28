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
level_files = ["level1.json", "level2.json", "level3.json"]  # fichiers JSON des niveaux

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

base_path = r"c:\Users\idimi\Documents\Codage\Python\ESGI-3SI4-TEAM1\jeux\jeux-plateforme2D"

idle_images=load_images_from_folder(os.path.join(base_path,"idle"))
run_images=load_images_from_folder(os.path.join(base_path,"run"))
jump_images=load_images_from_folder(os.path.join(base_path,"jump"))
fall_images=load_images_from_folder(os.path.join(base_path,"fall"))
attack_images=load_images_from_folder(os.path.join(base_path,"attack"))
crouch_images=load_images_from_folder(os.path.join(base_path,"crouch"))
slide_images=load_images_from_folder(os.path.join(base_path,"slide"))
dash_images=load_images_from_folder(os.path.join(base_path,"dash"))
dash_attack_images=load_images_from_folder(os.path.join(base_path,"dash_attack"))

# --- FOND MENU ---
menu_background_path = os.path.join(base_path,"forest.png")
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
        # invisible, donc rien à dessiner
        pass

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
    for i in range(len(level_files)):
        row=i//5
        col=i%5
        x=start_x+col*spacing_x
        y=start_y+row*spacing_y
        color=(200,200,200) if i!=selected_level else (255,255,0)
        pygame.draw.circle(screen,color,(x,y),circle_radius)
        pygame.draw.circle(screen,(0,0,0),(x,y),circle_radius,3)
        text=font.render(str(i+1),True,(0,0,0))
        screen.blit(text,(x-text.get_width()//2,y-text.get_height()//2))
    font_small=pygame.font.Font(None,30)
    info=font_small.render("Flèches : sélectionner, Entrée : jouer",True,(200,200,200))
    screen.blit(info,(WIDTH//2-info.get_width()//2,HEIGHT-50))
    pygame.display.flip()

def handle_level_select_event(event):
    global selected_level,state,player_x,player_y,platforms,barriers,scroll_x,background_image,level_data
    if event.key==pygame.K_LEFT:
        selected_level=(selected_level-1)%len(level_files)
    elif event.key==pygame.K_RIGHT:
        selected_level=(selected_level+1)%len(level_files)
    elif event.key==pygame.K_UP:
        if selected_level>=5:
            selected_level-=5
    elif event.key==pygame.K_DOWN:
        if selected_level<5:
            selected_level+=5
    elif event.key==pygame.K_RETURN:
        # --- Charger le niveau ---
        level_data = load_level_json(level_files[selected_level])
        if level_data:
            player_x,player_y = level_data["player_start"]
            platforms = [Platform(p["x"],p["y"],p["width"],p["height"]) for p in level_data["platforms"]]
            barriers = []
            if "barriers" in level_data:
                for b in level_data["barriers"]:
                    barriers.append(Barrier(b["x"], b["y"], b["width"], b["height"]))
            # Charger le fond du biome
            biome_path = os.path.join(base_path, "biome", level_data["biome"])
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
    # Vérifier les clés
    if "player_start" not in data or "platforms" not in data or "biome" not in data:
        print(f"❌ Niveau {filename} invalide !")
        return None
    return data

# --- GESTION ANIMATIONS ---
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
running=True
scroll_x=0
platforms=[]
barriers=[]
background_image=None
level_data=None

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if state==MENU:
                if event.key==pygame.K_DOWN:
                    selected_option=(selected_option+1)%len(menu_options)
                elif event.key==pygame.K_UP:
                    selected_option=(selected_option-1)%len(menu_options)
                elif event.key==pygame.K_RETURN:
                    if menu_options[selected_option]=="Jouer":
                        state=LEVEL_SELECT
                    elif menu_options[selected_option]=="Options":
                        state=OPTIONS
                    elif menu_options[selected_option]=="Quitter":
                        running=False
            elif state==LEVEL_SELECT:
                handle_level_select_event(event)
            elif state==OPTIONS:
                if event.key==pygame.K_ESCAPE:
                    state=MENU

    keys=pygame.key.get_pressed()

    # --- ETATS ---
    if state==MENU:
        draw_menu(screen)
        continue
    elif state==LEVEL_SELECT:
        draw_level_select(screen)
        continue
    elif state==OPTIONS:
        screen.fill((20,20,50))
        pygame.display.flip()
        continue
    elif state==GAME:
        moving=False
        player_velocity_x=0
        if keys[pygame.K_LEFT]:
            player_velocity_x=-PLAYER_SPEED
            moving=True
            facing_right=False
        if keys[pygame.K_RIGHT]:
            player_velocity_x=PLAYER_SPEED
            moving=True
            facing_right=True
        if keys[pygame.K_UP] and on_ground:
            player_velocity_y=JUMP_STRENGTH
            on_ground=False

        if dash_attack_cooldown_timer>0: dash_attack_cooldown_timer-=1
        if dash_cooldown_timer>0: dash_cooldown_timer-=1

        # Attaque normale
        if keys[pygame.K_a] and on_ground and not dashing_attack and not dashing:
            attacking = True
            attack_timer = len(attack_images) * ANIMATION_DELAY
            frame_indices["attack"] = 0
            animation_counters["attack"] = 0

        # Dash attack
        if keys[pygame.K_z] and on_ground and not dashing_attack and dash_attack_cooldown_timer==0:
            if keys[pygame.K_LEFT]:
                attacking=False
                dashing_attack=True
                dash_attack_timer=DASH_ATTACK_DURATION
                dash_attack_direction=-1
                dash_attack_cooldown_timer=DASH_ATTACK_COOLDOWN
            elif keys[pygame.K_RIGHT]:
                attacking=False
                dashing_attack=True
                dash_attack_timer=DASH_ATTACK_DURATION
                dash_attack_direction=1
                dash_attack_cooldown_timer=DASH_ATTACK_COOLDOWN

        # Dash normal
        if keys[pygame.K_d] and on_ground and not dashing and not dashing_attack and dash_cooldown_timer==0:
            if keys[pygame.K_LEFT]:
                dashing=True
                dash_timer=DASH_DURATION
                dash_direction=-1
                dash_cooldown_timer=DASH_COOLDOWN
            elif keys[pygame.K_RIGHT]:
                dashing=True
                dash_timer=DASH_DURATION
                dash_direction=1
                dash_cooldown_timer=DASH_COOLDOWN

        crouching=keys[pygame.K_DOWN] and on_ground

        # Physique
        if dashing_attack:
            player_velocity_x=dash_attack_direction*DASH_ATTACK_SPEED
        elif dashing:
            player_velocity_x=dash_direction*DASH_SPEED

        player_x+=player_velocity_x
        player_rect=pygame.Rect(player_x,player_y,50,50)

        # Collision plateformes et barrières (horizontal)
        for obj in platforms + barriers:
            if player_rect.colliderect(obj.rect):
                if player_velocity_x>0:
                    player_x=obj.rect.left-50
                elif player_velocity_x<0:
                    player_x=obj.rect.right
                player_rect.x=player_x

        player_velocity_y+=GRAVITY
        player_y+=player_velocity_y
        player_rect.y=player_y
        on_ground=False

        # Collision plateformes et barrières (vertical)
        for obj in platforms + barriers:
            if player_rect.colliderect(obj.rect):
                if player_velocity_y>0 and player_rect.bottom-player_velocity_y<=obj.rect.top+10:
                    player_y=obj.rect.top-50
                    player_velocity_y=0
                    on_ground=True
                    player_rect.y=player_y
                elif player_velocity_y<0 and player_rect.top-player_velocity_y>=obj.rect.bottom:
                    player_y=obj.rect.bottom
                    player_velocity_y=0
                    player_rect.y=player_y

        if player_y>HEIGHT+100:
            player_x,player_y=level_data["player_start"]
            player_velocity_y=0
            player_rect.x=player_x
            player_rect.y=player_y

        # Scroll
        if player_x-scroll_x>WIDTH*0.6:
            scroll_x=player_x-WIDTH*0.6
        elif player_x-scroll_x<WIDTH*0.3:
            scroll_x=player_x-WIDTH*0.3
        scroll_x=max(0,scroll_x)

        # Dessin
        if background_image:
            screen.blit(background_image,(0,0))
        else:
            screen.fill(BACKGROUND_COLOR)

        for plat in platforms:
            plat.draw(screen,scroll_x)

        current_frame=get_current_frame()
        screen.blit(current_frame,(player_x-scroll_x,player_y))

        # Barres
        bar_width=50
        bar_height=5
        bar_x=player_x-scroll_x
        bar_y=player_y-10
        max_cooldown=max(DASH_COOLDOWN,DASH_ATTACK_COOLDOWN)
        current_cooldown=max(dash_cooldown_timer,dash_attack_cooldown_timer)
        ratio=current_cooldown/max_cooldown if max_cooldown>0 else 0
        pygame.draw.rect(screen,(0,0,0),(bar_x,bar_y,bar_width,bar_height))
        pygame.draw.rect(screen,(0,0,255),(bar_x,bar_y,bar_width*ratio,bar_height))
        health_ratio=player_health/max_health
        pygame.draw.rect(screen,(0,0,0),(bar_x,bar_y-10,bar_width,bar_height))
        pygame.draw.rect(screen,(0,255,0),(bar_x,bar_y-10,bar_width*health_ratio,bar_height))

        pygame.display.flip()

pygame.quit()
