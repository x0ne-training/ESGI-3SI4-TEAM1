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

# --- Utility Functions ---
def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def create_board():
    """Creates an empty game board."""
    return [['.' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

def print_board(board, game_objects):
    """Prints the current state of the game board with game objects."""
    # Create a copy of the board to place objects on
    display_board = [row[:] for row in board]
    for obj in game_objects:
        if 0 <= obj.y < BOARD_HEIGHT and 0 <= obj.x < BOARD_WIDTH:
            display_board[obj.y][obj.x] = obj.char
    
    for row in display_board:
        print(" ".join(row))

def main():
    """Main function to run the game."""
    board = create_board()
    game_objects = []
    game_turn = 0

    while True:
        game_turn += 1
        clear_screen()
        print_board(board, game_objects)

        # Spawn a new zombie every 5 turns
        if game_turn % 5 == 0:
            spawn_y = random.randint(0, BOARD_HEIGHT - 1)
            game_objects.append(Zombie(BOARD_WIDTH - 1, spawn_y))

        # Get user input to place a plant
        # For now, we will simplify and not ask for input in the main loop
        # to focus on zombie movement first. We will re-integrate it later.
        
        time.sleep(1)

if __name__ == "__main__":
    main()