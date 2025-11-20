# Code for Commit 12
import time
import os
import random

# --- Game Configuration ---
BOARD_WIDTH = 10
BOARD_HEIGHT = 5
STARTING_SUN = 50

# --- Game Object Classes ---
class Plant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.char = 'P'
        self.cost = 50

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

def print_board(board, game_objects, sun, turn):
    display_board = [row[:] for row in board]
    for obj in game_objects:
        if 0 <= obj.y < BOARD_HEIGHT and 0 <= obj.x < BOARD_WIDTH:
            display_board[obj.y][obj.x] = obj.char
    
    print(f"Sun: {sun} | Turn: {turn}")
    for row in display_board:
        print(" ".join(row))

# --- Main Game Logic ---
def main():
    board = create_board()
    game_objects = []
    game_turn = 0
    sun = STARTING_SUN

    while True:
        game_turn += 1
        clear_screen()

        # --- UPDATE GAME STATE ---
        # (Game logic from previous commits: spawning, shooting, moving, collision)
        if game_turn % 5 == 0:
            game_objects.append(Zombie(BOARD_WIDTH - 1, random.randint(0, BOARD_HEIGHT - 1)))
        
        new_peas = [Pea(obj.x + 1, obj.y) for obj in game_objects if isinstance(obj, Plant)]
        game_objects.extend(new_peas)

        for obj in game_objects:
            if isinstance(obj, Zombie): obj.x -= 1
            elif isinstance(obj, Pea): obj.x += 1
        
        peas_to_remove, zombies_to_remove = [], []
        for pea in [p for p in game_objects if isinstance(p, Pea)]:
            for zombie in [z for z in game_objects if isinstance(z, Zombie)]:
                if pea.x == zombie.x and pea.y == zombie.y:
                    zombie.health -= 1
                    if pea not in peas_to_remove: peas_to_remove.append(pea)
                    if zombie.health <= 0 and zombie not in zombies_to_remove: zombies_to_remove.append(zombie)
        
        game_objects = [obj for obj in game_objects if obj not in peas_to_remove and obj not in zombies_to_remove and not (isinstance(obj, Pea) and obj.x >= BOARD_WIDTH)]

        # --- DRAW THE BOARD ---
        print_board(board, game_objects, sun, game_turn)

        # --- GET USER INPUT ---
        action = input("Press 'p' to plant (cost 50), or Enter to continue: ")
        if action.lower() == 'p':
            plant_cost = Plant(0, 0).cost
            if sun >= plant_cost:
                try:
                    plant_y = int(input(f"Enter row (0-{BOARD_HEIGHT-1}): "))
                    plant_x = int(input(f"Enter col (0-{BOARD_WIDTH-1}): "))
                    if 0 <= plant_y < BOARD_HEIGHT and 0 <= plant_x < BOARD_WIDTH:
                        game_objects.append(Plant(plant_x, plant_y))
                        sun -= plant_cost
                    else:
                        print("Invalid coordinates.")
                        time.sleep(1)
                except ValueError:
                    print("Invalid input. Please enter numbers.")
                    time.sleep(1)
            else:
                print("Not enough sun!")
                time.sleep(1)
        
        # A small delay to make the game playable without input
        time.sleep(0.5)

if __name__ == "__main__":
    main()
