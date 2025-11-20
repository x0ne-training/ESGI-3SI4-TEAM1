# Code for Commit 13
import time
import os
import random

# --- Game Configuration ---
BOARD_WIDTH = 10
BOARD_HEIGHT = 5
STARTING_SUN = 50

# --- Game Object Classes (Same as before) ---
class Plant:
    def __init__(self, x, y): self.x, self.y, self.char, self.cost = x, y, 'P', 50
class Zombie:
    def __init__(self, x, y): self.x, self.y, self.char, self.health = x, y, 'Z', 3
class Pea:
    def __init__(self, x, y): self.x, self.y, self.char = x, y, '-'

# --- Utility Functions (Same as before) ---
def clear_screen(): os.system('cls' if os.name == 'nt' else 'clear')
def create_board(): return [['.' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
def print_board(board, game_objects, sun, turn):
    display_board = [row[:] for row in board]
    for obj in game_objects:
        if 0 <= obj.y < BOARD_HEIGHT and 0 <= obj.x < BOARD_WIDTH:
            display_board[obj.y][obj.x] = obj.char
    print(f"Sun: {sun} | Turn: {turn}")
    for row in display_board: print(" ".join(row))

# --- Main Game Logic ---
def main():
    board = create_board()
    game_objects = []
    game_turn = 0
    sun = STARTING_SUN
    game_over = False # Game over flag

    while not game_over:
        game_turn += 1
        clear_screen()

        # --- UPDATE GAME STATE ---
        # (Same logic as before)
        if game_turn % 5 == 0: game_objects.append(Zombie(BOARD_WIDTH - 1, random.randint(0, BOARD_HEIGHT - 1)))
        game_objects.extend([Pea(obj.x + 1, obj.y) for obj in game_objects if isinstance(obj, Plant)])
        for obj in game_objects:
            if isinstance(obj, Zombie): obj.x -= 1
            elif isinstance(obj, Pea): obj.x += 1
        
        peas_to_remove, zombies_to_remove = [], []
        for p in [o for o in game_objects if isinstance(o, Pea)]:
            for z in [o for o in game_objects if isinstance(o, Zombie)]:
                if p.x == z.x and p.y == z.y:
                    z.health -= 1
                    if p not in peas_to_remove: peas_to_remove.append(p)
                    if z.health <= 0 and z not in zombies_to_remove: zombies_to_remove.append(z)
        game_objects = [o for o in game_objects if o not in peas_to_remove and o not in zombies_to_remove and not (isinstance(o, Pea) and o.x >= BOARD_WIDTH)]

        # Check for game over condition
        for obj in game_objects:
            if isinstance(obj, Zombie) and obj.x < 0:
                game_over = True
                break

        # --- DRAW THE BOARD ---
        print_board(board, game_objects, sun, game_turn)

        # --- GET USER INPUT (only if game is not over) ---
        if not game_over:
            action = input("Press 'p' to plant (cost 50), or Enter to continue: ")
            if action.lower() == 'p':
                if sun >= Plant(0,0).cost:
                    try:
                        y = int(input(f"Row (0-{BOARD_HEIGHT-1}): "))
                        x = int(input(f"Col (0-{BOARD_WIDTH-1}): "))
                        game_objects.append(Plant(x, y))
                        sun -= Plant(0,0).cost
                    except (ValueError, IndexError): print("Invalid location.")
                else: print("Not enough sun!")
            time.sleep(0.5)

    # --- GAME OVER SCREEN ---
    clear_screen()
    print("=================")
    print("    GAME OVER    ")
    print("The zombies ate your brains!")
    print("=================")

if __name__ == "__main__":
    main()
