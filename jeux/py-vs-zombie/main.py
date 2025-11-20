# Code for Commit 15
import time
import os
import random

# --- Game Configuration ---
BOARD_WIDTH = 10
BOARD_HEIGHT = 5
STARTING_SUN = 50

# --- Game Object Classes ---

class Plant: # Base Plant class
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.char = 'P'
        self.cost = 50

class Sunflower(Plant): # New Sunflower class
    def __init__(self, x, y):
        super().__init__(x, y)
        self.char = 'S'
        self.cost = 25
        self.sun_production_rate = 5 # produces sun every 5 turns
        self.sun_amount = 25

class Zombie: # Base Zombie class
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.char = 'Z'
        self.health = 3

class BucketheadZombie(Zombie): # New tougher Zombie
    def __init__(self, x, y):
        super().__init__(x, y)
        self.char = 'B'
        self.health = 6

class Pea:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.char = '-'

# --- Utility Functions (Same as Commit 14) ---
def clear_screen(): os.system('cls' if os.name == 'nt' else 'clear')
def create_board(): return [['.' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
def print_board(board, game_objects, sun, turn):
    display_board = [row[:] for row in board]
    for obj in game_objects:
        if 0 <= obj.y < BOARD_HEIGHT and 0 <= obj.x < BOARD_WIDTH: display_board[obj.y][obj.x] = obj.char
    print("--- Plants vs Zombies ---")
    print(f"Sun: {sun} | Turn: {turn}")
    print("-" * (BOARD_WIDTH * 2 + 3))
    for row in display_board: print("| " + " ".join(row) + " |")
    print("-" * (BOARD_WIDTH * 2 + 3))

# --- Main Game Logic ---
def main():
    board = create_board()
    game_objects = []
    game_turn = 0
    sun = STARTING_SUN
    game_over = False

    while not game_over:
        game_turn += 1
        clear_screen()

        # --- UPDATE GAME STATE ---

        # 1. Sun generation (passive and from sunflowers)
        if game_turn % 4 == 0: sun += 25
        for obj in game_objects:
            if isinstance(obj, Sunflower) and game_turn % obj.sun_production_rate == 0:
                sun += obj.sun_amount
        
        # 2. Spawn different zombie types
        if game_turn % 7 == 0: # Bucketheads are less frequent
            game_objects.append(BucketheadZombie(BOARD_WIDTH - 1, random.randint(0, BOARD_HEIGHT - 1)))
        elif game_turn % 5 == 0:
            game_objects.append(Zombie(BOARD_WIDTH - 1, random.randint(0, BOARD_HEIGHT - 1)))
            
        # 3. Plants shoot (only Peashooters, not Sunflowers)
        game_objects.extend([Pea(obj.x + 1, obj.y) for obj in game_objects if isinstance(obj, Plant) and not isinstance(obj, Sunflower)])

        # 4. Move objects
        for obj in game_objects:
            if isinstance(obj, Zombie): obj.x -= 1
            elif isinstance(obj, Pea): obj.x += 1
            
        # 5. Collisions
        peas_to_remove, zombies_to_remove = [], []
        for p in [o for o in game_objects if isinstance(o, Pea)]:
            for z in [o for o in game_objects if isinstance(o, Zombie)]:
                if p.x == z.x and p.y == z.y:
                    z.health -= 1
                    if p not in peas_to_remove: peas_to_remove.append(p)
                    if z.health <= 0 and z not in zombies_to_remove: zombies_to_remove.append(z)
        
        # 6. Remove objects
        game_objects = [o for o in game_objects if o not in peas_to_remove and o not in zombies_to_remove and not (isinstance(o, Pea) and o.x >= BOARD_WIDTH)]

        # 7. Check for Game Over
        if any(isinstance(obj, Zombie) and obj.x < 0 for obj in game_objects): game_over = True

        # --- DRAW BOARD & GET INPUT ---
        print_board(board, game_objects, sun, game_turn)
        if not game_over:
            action = input("Plant 'p'eashooter (50), 's'unflower (25), or Enter: ")
            if action.lower() == 'p' or action.lower() == 's':
                is_peashooter = action.lower() == 'p'
                plant_class = Plant if is_peashooter else Sunflower
                cost = plant_class(0,0).cost
                
                if sun >= cost:
                    try:
                        y = int(input(f"Row (0-{BOARD_HEIGHT-1}): ")); x = int(input(f"Col (0-{BOARD_WIDTH-1}): "))
                        game_objects.append(plant_class(x, y)); sun -= cost
                    except (ValueError, IndexError): print("Invalid location.")
                else: print("Not enough sun!")
            time.sleep(0.5)

    # --- GAME OVER SCREEN ---
    clear_screen()
    print("=================\n    GAME OVER    \nThe zombies ate your brains!\n=================")

if __name__ == "__main__":
    main()
