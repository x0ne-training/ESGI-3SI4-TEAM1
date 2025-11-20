# Code for Commit 10
import time
import os
import random

# --- Game Configuration ---
BOARD_WIDTH = 10
BOARD_HEIGHT = 5

# --- Game Object Classes ---
class Plant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.char = 'P'

class Zombie:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.char = 'Z'
        self.health = 3

class Pea:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.char = '-'

# --- Utility Functions ---
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_board():
    return [['.' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

def print_board(board, game_objects):
    display_board = [row[:] for row in board]
    for obj in game_objects:
        if 0 <= obj.y < BOARD_HEIGHT and 0 <= obj.x < BOARD_WIDTH:
            display_board[obj.y][obj.x] = obj.char
    
    for row in display_board:
        print(" ".join(row))

# --- Main Game Logic ---
def main():
    board = create_board()
    game_objects = []
    game_turn = 0 # Added game turn counter

    game_objects.append(Plant(1, 2))

    while True:
        game_turn += 1
        clear_screen()

        # --- UPDATE GAME STATE ---

        # 1. Spawn new zombies periodically
        if game_turn % 5 == 0:
            spawn_y = random.randint(0, BOARD_HEIGHT - 1)
            game_objects.append(Zombie(BOARD_WIDTH - 1, spawn_y))

        # 2. Plants shoot
        new_peas = []
        for obj in game_objects:
            if isinstance(obj, Plant):
                new_peas.append(Pea(obj.x + 1, obj.y))
        game_objects.extend(new_peas)

        # 3. Move objects
        for obj in game_objects:
            if isinstance(obj, Zombie):
                obj.x -= 1
            elif isinstance(obj, Pea):
                obj.x += 1
        
        # 4. Collision Detection and Damage
        peas_to_remove = []
        zombies_to_remove = []
        
        for pea in [p for p in game_objects if isinstance(p, Pea)]:
            for zombie in [z for z in game_objects if isinstance(z, Zombie)]:
                if pea.x == zombie.x and pea.y == zombie.y:
                    zombie.health -= 1
                    if pea not in peas_to_remove:
                        peas_to_remove.append(pea)
                    if zombie.health <= 0 and zombie not in zombies_to_remove:
                        zombies_to_remove.append(zombie)
        
        # 5. Remove dead objects and off-screen peas
        game_objects = [
            obj for obj in game_objects 
            if obj not in peas_to_remove 
            and obj not in zombies_to_remove
            and not (isinstance(obj, Pea) and obj.x >= BOARD_WIDTH)
        ]

        # --- DRAW THE BOARD ---
        print(f"Turn: {game_turn}")
        print_board(board, game_objects)
        
        time.sleep(1)

if __name__ == "__main__":
    main()
