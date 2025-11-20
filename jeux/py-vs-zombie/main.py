# Code for Commit 8
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

    game_objects.append(Plant(1, 2))
    game_objects.append(Zombie(8, 2))

    while True:
        clear_screen()

        # --- UPDATE GAME STATE ---

        # 1. Plants shoot
        new_peas = []
        for obj in game_objects:
            if isinstance(obj, Plant):
                new_peas.append(Pea(obj.x + 1, obj.y))
        game_objects.extend(new_peas)

        # 2. Move objects
        for obj in game_objects:
            if isinstance(obj, Zombie):
                obj.x -= 1
            elif isinstance(obj, Pea):
                obj.x += 1
        
        # 3. Collision Detection
        peas = [p for p in game_objects if isinstance(p, Pea)]
        zombies = [z for z in game_objects if isinstance(z, Zombie)]
        collided_peas = []

        for pea in peas:
            for zombie in zombies:
                if pea.x == zombie.x and pea.y == zombie.y:
                    collided_peas.append(pea)
        
        # 4. Remove collided and off-screen objects
        surviving_objects = []
        for obj in game_objects:
            # Keep object if it's not a collided pea
            is_collided_pea = obj in collided_peas
            # Keep object if it's a pea within the board boundaries
            is_on_screen_pea = isinstance(obj, Pea) and obj.x < BOARD_WIDTH
            # Keep any non-pea object
            is_other_object = not isinstance(obj, Pea)

            if not is_collided_pea and (is_on_screen_pea or is_other_object):
                surviving_objects.append(obj)
        
        game_objects = surviving_objects

        # --- DRAW THE BOARD ---
        print_board(board, game_objects)
        
        time.sleep(1)

if __name__ == "__main__":
    main()
