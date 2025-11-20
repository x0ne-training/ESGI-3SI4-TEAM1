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

# --- Main Game Logic ---
def main():
    """Main function to run the game."""
    board = create_board()
    game_objects = [Plant(1, 2)] # Start with one plant for testing
    game_turn = 0

    while True:
        game_turn += 1
        clear_screen()

        # Plants shoot every 3 turns
        if game_turn % 3 == 0:
            for obj in game_objects:
                if isinstance(obj, Plant):
                    game_objects.append(Pea(obj.x + 1, obj.y))

        # Update game state
        for obj in game_objects:
            if isinstance(obj, Zombie):
                obj.x -= 1

        print_board(board, game_objects)

        # Spawn a new zombie every 5 turns
        if game_turn % 5 == 0:
            spawn_y = random.randint(0, BOARD_HEIGHT - 1)
            game_objects.append(Zombie(BOARD_WIDTH - 1, spawn_y))
        
        time.sleep(1)

if __name__ == "__main__":
    main()