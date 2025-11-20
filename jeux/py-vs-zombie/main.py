import time
import os

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

# --- Main Game Logic ---
def main():
    """Main function to run the game."""
    board = create_board()
    game_objects = [Plant(1, 2), Zombie(8, 2)]
    while True:
        clear_screen()
        print_board(board, game_objects)
        time.sleep(1)

def main():
    """Main function to run the game."""
    board = create_board()
    game_objects = []
    
    while True:
        clear_screen()
        print_board(board, game_objects)
        
        # Get user input to place a plant
        try:
            plant_y = int(input(f"Enter row to plant (0-{BOARD_HEIGHT-1}): "))
            plant_x = int(input(f"Enter col to plant (0-{BOARD_WIDTH-1}): "))
            if 0 <= plant_y < BOARD_HEIGHT and 0 <= plant_x < BOARD_WIDTH:
                game_objects.append(Plant(plant_x, plant_y))
        except ValueError:
            print("Invalid input. Please enter a number.")

        time.sleep(1)

if __name__ == "__main__":
    main()